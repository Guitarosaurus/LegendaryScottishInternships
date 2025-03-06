from django import forms
from legendary.models import Company, Internship, Comment, UserProfile
from django.conrtib.auth.models import User

class UserForm(forms.ModelForm):
    # Overrides so that password is not visible for everyone to see
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile',)


class CompanyForm(forms.ModelForm):
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

class InternshipForm(forms.ModelForm):
    name = forms.CharField(Internship.MAX_NAME_LENGTH, unique = True,
                           help_text="Please enter the internship name.")
    description = forms.CharField(Internship.MAX_DESC_LENGTH, 
                                  help_text="Please enter a description.")
    closing_date = forms.DateField(help_text="Please enter the closing date.")
    start_date = forms.DateField(help_text="Please enter the start date.")
    end_date = forms.DateField(help_text="Please enter the end date.")
    salary = forms.FloatField(help_text="Please enter the salary.")
    # Company_Id not entered?
    address = forms.CharField(Internship.MAX_ADDR_LENGTH,
                              help_text = "Please enter the address")
    # Not sure if there is a better way to enter the checklist
    checklist = forms.CharField(Internship.MAX_LIST_LENGTH,
                                help_text="Please enter items required")
    slug = forms.CharField(unique = True, required=False)

    class Meta:
        model = Internship
        # not sure about this
        exclude = ('company_id', 'user_ids',)