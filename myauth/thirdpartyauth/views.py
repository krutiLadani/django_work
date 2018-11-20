from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from .forms import UserAuth


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UserAuth(request.POST)
        if form.is_valid:
            print("=========form valid==============")
            user_name = form.cleaned_data['user_name']
            pswd = form.cleaned_data['pswd']
            return render(request, 'thirdpartyauth/home.html', {'form': form, 'errors': form.errors})
        else:
            print("form invalid")
            return render(request, 'thirdpartyauth/home.html', {'form': form, 'errors': form.errors})

    if request.method == 'GET':
        form = UserAuth(request.GET)
        return render(request, 'thirdpartyauth/home.html', {'form': form})

   # return render(request,'thirdpartyauth/home.html')
