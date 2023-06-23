from base64 import urlsafe_b64decode
from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
from LolSwagg.settings import MESSAGE_TAGS
from accounts.models import Account
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username= email.split('@')[0]
            user= Account.objects.create_user(first_name=first_name,last_name=last_name,email=email, username=username, password=password)
            user.phone_number = phone_number
            user.address = address 
            user.save()
            return redirect('login')
    else:
        form= RegistrationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/register.html', context)



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate( email=email, password=password )
        if user is not None:
            pass
            auth.login(request, user)
            messages.success(request,'you are now logged in')
            return redirect('dashboard')
        else:
             messages.error(request,'invalid information')
        
    return render(request, 'accounts/login.html')
@login_required( login_url = 'login' )
def logout(request):
    auth.logout(request)
    messages.success(request, 'you are logged out succesfuly')
    return redirect('dashboard')

def dashboard(request):
    return render(request, 'accounts/dashbord.html')
