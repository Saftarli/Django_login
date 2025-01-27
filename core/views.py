from pyexpat.errors import messages

from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import  reverse_lazy
from django.views.generic import CreateView
from core.forms import CustomRegisterForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import  messages
from django.http import HttpResponse
from core.models import CustomUser
from django.contrib.auth import logout, login, authenticate


# Create your views here.

def index(request):
     return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.id).encode())
            current_site = get_current_site(request)
            mail_subjects = 'confirmation of account registration'
            message = render_to_string('account/activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
            })
            send = send_mail(mail_subjects, message, settings.EMAIL_HOST_USER, [user.email])
            messages.success(request, 'Tesdiq linki gonderildi gir bax cixarsan')
            return redirect('login')
        else:
            form = CustomRegisterForm()

    else:
        form = CustomRegisterForm()
    return  render(request, 'account/register.html', context={'form': form})

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email, "###########################")
        password = request.POST.get('password')
        print(password, "SIFREER ##############")
        user = authenticate(request, username=email, password=password)
        print(user, 'tapildi#########################################')
        if user is not None:
            login(request, user)
            messages.success('Siz daxil oldunuz')
            return redirect('home')
    return render(request, 'account/login.html')

    return render(request, 'account/login.html')

def logout(request):
    pass

def verify(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Hesabiniz tesdiqlendi')
        else:
            return HttpResponse('link etibarsizdir')

    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):

        return HttpResponse('link etibarsizdir')
