from django import forms
from legendary.models import Company, Internship, Comment
from django.conrtib.auth.models import User

class UserLoginForm(forms.ModelForm):
    # Overrides so that password is not visible for everyone to see
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'passowrd',)

class CompanyForm(form.modelForm):
    name = forms.CharField(max_length=Company.MAX_NAME_LENGTH, 
                            help_text = "Please enter company name.",
                            unique = True)
    address = forms.CharField(max_length=Company.MAX_ADDR_LENGTH,
                            help_text="Please enter a company address.")
    email = forms.CharField(max_length=Company.MAX_EMAIL_LENGTH,
                            help_text="Please enter an company email.",
                            unique = True)
    website = forms.CharField(max_length=Company.MAX_URL_LENGTH,
                              help_text="Please enter company website",
                              unique = True)
    
    class Meta:
        model = Company
        fields = ('name', 'address', 'email', 'website',)