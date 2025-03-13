from django import forms
from legendary.models import Company, Internship, Comment, UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    # Overrides so that password is not visible for everyone to see
    password = forms.CharField(widget=forms.PasswordInput(), 
                               help_text="Please make sure password is minimum 6 characters")

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class CompanyForm(forms.ModelForm):
    name = forms.CharField(max_length=Company.MAX_NAME_LENGTH, 
<<<<<<< HEAD
                            help_text = "Please enter company name.")
    address = forms.CharField(max_length=Company.MAX_ADDR_LENGTH,
                            help_text="Please enter a company address.")
    email = forms.CharField(max_length=Company.MAX_EMAIL_LENGTH,
                            help_text="Please enter an company email.")
    website = forms.CharField(max_length=Company.MAX_URL_LENGTH,
                              help_text="Please enter company website")
=======
                            help_text = "Please enter company name.",)
    address = forms.CharField(max_length=Company.MAX_ADDR_LENGTH,
                            help_text="Please enter a company address.")
    email = forms.CharField(max_length=Company.MAX_EMAIL_LENGTH,
                            help_text="Please enter an company email.",)
    website = forms.CharField(max_length=Company.MAX_URL_LENGTH,
                              help_text="Please enter company website",)
>>>>>>> d4988a4 (update forms mistake: max_length assignment)
    
    class Meta:
        model = Company
        fields = ('name', 'address', 'email', 'website',)

class InternshipForm(forms.ModelForm):
    name = forms.CharField(max_length=Internship.MAX_NAME_LENGTH,
<<<<<<< HEAD
                           help_text="Please enter the internship name.")
=======
                           help_text="Please enter the internship name.",)
>>>>>>> d4988a4 (update forms mistake: max_length assignment)
    description = forms.CharField(max_length=Internship.MAX_DESC_LENGTH, 
                                  help_text="Please enter a description.")
    closing_date = forms.DateField(help_text="Please enter the closing date.")
    start_date = forms.DateField(help_text="Please enter the start date.")
    end_date = forms.DateField(help_text="Please enter the end date.")
    salary = forms.FloatField(help_text="Please enter the salary.")
    # Company_Id not entered?
    address = forms.CharField(max_length=Internship.MAX_ADDR_LENGTH,
                              help_text = "Please enter the address")
    # Not sure if there is a better way to enter the checklist
    checklist = forms.CharField(max_length=Internship.MAX_LIST_LENGTH,
                                help_text="Please enter items required")
<<<<<<< HEAD
    slug = forms.CharField( required=False)
=======
    #slug = forms.CharField(unique = True, required=False)
>>>>>>> d4988a4 (update forms mistake: max_length assignment)

    class Meta:
        model = Internship
        exclude = ('company_id', 'user_ids',)

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=Comment.MAX_COMMENT_LENGTH)
    # Rest of fields filled in by login details?

    class Meta:
        model = Comment
        fields = ('name', )

class ChangeChecklistForm(forms.ModelForm):
    checklist = forms.CharField(max_length=Internship.MAX_LIST_LENGTH, 
                                help_text = "Please enter the updated checkist")
    
    class Meta:
        fields = ('name',)
