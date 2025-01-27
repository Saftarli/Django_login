from django import forms
from .models import CustomUser
from django_recaptcha.widgets import  ReCaptchaV2Checkbox
from django_recaptcha.fields import ReCaptchaField

class CustomRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    class Meta:
        model = CustomUser
        fields = ('email','password')
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered')
        return email



