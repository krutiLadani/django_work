# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from forms import SignUpForm,Checkout
from django.contrib.auth.decorators import login_required
from .models import Product,Cart
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View
from shop.utils import render_to_pdf
from django.template.loader import get_template 
from django.views import generic
import uuid
from django.core.mail import send_mail




def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects   
    products = Product.objects.all().order_by('id')
    page = request.GET.get('page',1)
    paginator = Paginator(products, 2)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "products": products,
    }
    return render(request,'index.html', context,)


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:   
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index')
        else:
            form = SignUpForm()
    return render(request, 'shop/signup.html', {'form': form})



def home(request):
    return render(request, 'shop/home.html')



def details(request,pk):
    try:
        product_id = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request,'shop/details.html',context={'product':product_id,})


def add_cart(request):
    data = Cart.objects.filter(uname__username=request.user.username)   
    context = {
    "product_number": data
    }
    return render(request, 'shop/cart.html',context)


def order(request):
    data = Cart.objects.filter(uname__username=request.user.username)   
    data1 = Cart.objects.filter(uname__username=request.user.username).aggregate(Sum('total_price')).values()[0]
    context = {
    "product_number": data,
    "price": data1,
    }
    return render(request, 'shop/checkout.html',context)

    
@csrf_exempt
@login_required(login_url='shop/accounts/login/')
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id', '')
        cart_d = request.POST.get('total_product', '')
        user = User.objects.get(username = request.user.username)
        product = Product.objects.get(id = product_id)
        data = {}   
        cart, created = Cart.objects.get_or_create(uname=user, product_detail=product)
        cart.total_product = cart_d
        cart.total_price=int(product.product_price)*int(cart_d)
        cart.save()
        data['success'] = True
        data['cart_url'] = reverse('cart')
        data['total_product'] = cart_d
        data['total_price'] = cart.total_price
        data['product_id'] = product.id
    else:
        data['success'] = False
    return JsonResponse(data)


@csrf_exempt
def cart_remove(request, product_id):
    if request.method == 'POST':
        product_id = request.POST.get('product_id', '')
        username = request.POST.get('username','')
        user = User.objects.get(username = username)
        product = Cart.objects.get(id = product_id)
        data = {}   
        cartItems = Cart.objects.filter(uname=request.user, product_detail=product.product_detail)
        cartItems.delete()
        data['success'] = True
        data['product_id'] = product_id
    else:
        data['success'] = False
    return JsonResponse(data)


def checkout(request):
    if request.method == 'POST':
        form = Checkout(request.POST)
        phoneno = request.POST.get('phone_no', '') 
        address = request.POST.get('address', '')
        zip = request.POST.get('zip', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        if form.is_valid():
            profile_obj = form.save(commit=False)
            profile_obj.user = request.user
            form.save(commit=True)
            return redirect('index')
    else: 
        form = Checkout()
    return render(request, 'shop/checkout.html', {'form': form})



class GeneratePDF(generic.DetailView):
     def get(self, request, *args, **kwargs):
         template = get_template('shop/invoice.html')
         data = Cart.objects.filter(uname__username=request.user.username)
         data1 = Cart.objects.filter(uname__username=request.user.username).aggregate(Sum('total_price')).values()[0]
         context = {
             "invoice_id": uuid.uuid4(),
             "product_number": data,
             "customer_name": request.user.username,
             "amount":data1,
         }
         send_mail('pdf', 'Shopping Receipt', 'kruti.ladani@gmail.com', ['kruti29.ladani@gmail.com'], fail_silently=False)
         html = template.render(context)
         pdf = render_to_pdf('shop/invoice.html', context)
         if pdf:
             response = HttpResponse(pdf, content_type='application/pdf')
             filename = "Invoice_%s.pdf" %("12341231")
             content = "inline; filename='%s'" %(filename)
             download = request.GET.get("download")
             if download:
                 content = "attachment; filename='%s'" %(filename)
             response['Content-Disposition'] = content
             return response
         return HttpResponse("Not found")


