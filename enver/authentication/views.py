from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import CustomUser
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'This email is already registered. Please log in.')
                return redirect('login_user')

            CustomUser.objects.create(email=email, password=password)
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login_user')
    else:
        form = RegistrationForm()

    return render(request, 'authentication/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = CustomUser.objects.filter(email=email, password=password).first()
            if user:
                return redirect('contact_form:contact-form')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})
