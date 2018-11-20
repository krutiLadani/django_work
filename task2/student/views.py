from django.shortcuts import render, render_to_response
from django.http import JsonResponse, HttpResponse
from .forms import SignUpForm, FeepaymentForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Student, Institute, Branch, FeeType, Fee, Transaction
import razorpay
from django.template.loader import get_template
from xhtml2pdf import pisa


# from student.utils import render_to_pdf
# Create your views here.

def student_index(request):
    return render(request,'student/student_index.html')


def registration(request):
    return render(request,'student/registration.html')


@csrf_exempt
def get_branches(request):
    if request.method == 'POST':
        data = []
        institute =  request.POST.get('countryId', '')
        
        option = "<option option=''> --------</option>"
        # branches = Branch.objects.get(institute=institute)
        for branch in Branch.objects.filter(institute=institute, is_active=True):
            option += "<option value=" + str(branch.id) + ">" + branch.name + "</option>," 
            # option = "<option value=branch.id>branch.name</option>"
            # data.append(str(option))
    return HttpResponse(option)


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("form valid")
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            contact = form.cleaned_data.get('contact')
            enrol_no = form.cleaned_data.get('enrol_no')
            institute = form.cleaned_data.get('institute')
            branch = form.cleaned_data.get('branch')
            course = form.cleaned_data.get('course')
            birth_date = form.cleaned_data.get('birth_date')

            st = Student.objects.create(user=user,enrol_no=enrol_no,contact=contact,institute=institute,branch=branch,course=course,birth_date=birth_date)
            form = SignUpForm(request.GET)
            return render(request, 'student/signup.html', {'form': form, 'errors': form.errors})
        else:
            print("form invalid")
            return render(request, 'student/signup.html', {'form': form, 'errors': form.errors})

    if request.method == 'GET':
        form = SignUpForm(request.GET)
        return render(request, 'student/signup.html', {'form': form})

def fees(request):
    if request.method == 'POST':
        form = FeepaymentForm(request.POST)
        if form.is_valid():
            form = FeepaymentForm(request.GET)
            # fee_type = FeeType.objects.all()
            fee_type =  FeeType.objects.filter(is_active=True)
            print("===fee_type===",fee_type)
            return render(request, 'student/fees.html', {'form': form, 'errors': form.errors, 'fee_type':fee_type})
        else:
            print("form invalid")
            return render(request, 'student/fees.html', {'form': form, 'errors': form.errors})

    if request.method == 'GET':
        # fee_type = FeeType.objects.all()
        fee_type =  FeeType.objects.filter(is_active=True)
        print("===fee_type===",fee_type)
        form = FeepaymentForm(request.GET)
        form = FeepaymentForm(request.GET)
        user = request.user
        return render(request, 'student/fees.html', {'form': form,'fee_type':fee_type, 'user':user})

@csrf_exempt
def calculate_fees(request):
    data = {}
    if request.method == 'POST':
        fee_id = request.POST.get('fee_id', '')
        status = request.POST.get('status', '')
        fee = FeeType.objects.get(id=fee_id)
        amount = fee.amount
        if status == 'true':
            data['amount'] = amount
        else:
            data['amount'] = -amount
    else:
        data['success'] = False
    return JsonResponse(data)

@csrf_exempt
def final_amount(request):
    data = {}
    if request.method == 'POST':
        exam_name = request.POST.getlist('name_array[]')
        amount = 0
        for exam in exam_name:
            ft = FeeType.objects.get(name=exam)
            amount += ft.amount
            data['amount'] = amount
    else:
        data['success'] = False
    print(data)
    return JsonResponse(data)

@csrf_exempt
def add_fees(request):
    data = {}
    if request.method == 'POST':
        amount = request.POST.get('amount', '')
        exam_name = request.POST.getlist('name_array[]')
        payment_id = request.POST.get('payment_id', '')
        user = request.user
        # fee_id = Fee.objects.create(user=user, amount=amount, payment_id=payment_id)
        fee_id,created = Fee.objects.get_or_create(user=user)
        fee_id.amount= amount
        fee_id.payment_id= payment_id

        for exam in exam_name:
            ft = FeeType.objects.get(name=exam)
            fee_id.fees_paid.add(ft) 
        fee_id.save()
        client = razorpay.Client(auth=("rzp_test_BIGjC2BDYG3x1c", "5yLDMLqsfmjTNTL40zrmOKXh"))
        api_response = client.payment.fetch(payment_id)
        if not api_response.get('error_code'):
            # uuid = api_response.get('id')
            paid_amt = api_response.get('amount')/100
            status = api_response.get('status')
            request_dump = api_response
            Transaction.objects.create(payment_id=payment_id, user=user, paid_amt=paid_amt, status=status, request_dump=request_dump)
        data['success'] = True
    else:
        data['success'] = False
    return JsonResponse(data)


def render_pdf_view(request):
    print("====render_pdf_view===")
    template_path = 'student/invoice.html'
    fee = Fee.objects.filter(user=request.user).order_by('-id')[0]
    fee_types = fee.fees_paid.all()

    context = {
        'payment_id': fee.payment_id,
        'fees' : fee_types,
         'user' : request.user,
         'total' : fee.amount,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
