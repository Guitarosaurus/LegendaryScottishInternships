from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from legendary.forms import UserForm,UserProfileForm,CompanyForm,InternshipForm,CommentForm,ChangeChecklistForm
from legendary.models import Company, Internship, Comment, UserProfile
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from email.message import EmailMessage
import smtplib, ssl



def index(request):

    context_dict = {}

    
    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'legendary/index.html', context=context_dict)

    # Return response back to the user, updating any cookies that need changed.
    return response

def about(request):

    context_dict = {}
    response = render(request, 'legendary/about.html', context=context_dict)

    return response

def report(request, internship_name, email_content):
    
    password = "Legendary$cottishInternships" # This isn't secure, but no-one should be able to access this source code
    msg = EmailMessage()
    msg.set_content(email_content)
    msg['Subject'] = "Internship Reported - " + internship_name
    msg['From'] = "LegendaryScottishInternships@gmx.com"
    msg['To'] = "LegendaryScottishInternships@gmx.com"

    context = ssl.create_default_context()
    s = smtplib.SMTP('mail.gmx.com', 587)
    s.starttls(context=context)
    s.login(msg['From'], password)
    s.send_message(msg)
    s.quit()

    return redirect(reverse('legendary:listings'))

@login_required
def profile(request):
    response = render(request, 'legendary/profile.html')

    return response

@login_required
def update_profile(request):

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/legendary/profile/')
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)


    response = render(request, 'legendary/update-profile.html', {'form': form})

    return response

@login_required
def change_checklist(request):

    if request.method == "POST":
        form = ChangeChecklistForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            #wondering the best redirect here
            # Took out html so redirect works
            return redirect('/legendary/profile/')
    
        else:
            print(form.errors) 
    else:
        form = ChangeChecklistForm(instance=request.user)  
    
    response = render(request, 
                      'legendary/update-checklist.html', 
                      {'form': form})
    
    return response

def user_login(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request,user)
                return redirect(reverse('legendary:index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'legendary/login.html')


def register(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    response = render(request, 
                      'legendary/register.html', 
                      context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})

    return response

@login_required
def comment(request, internship_id, comment_data):

    if request.method == 'GET':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.internship_id = Internship.objects.get(name=internship_id)
            comment.data = comment_data
            comment.user_id = request.user
            comment.save()
            
        else:
            print(comment_form.errors)
    else:
        comment_form = CommentForm()

    return redirect(reverse('legendary:listings'))

def listings(request):

    context_dict = {}
    context_dict['listings'] = Internship.objects.order_by('-name')
    response = render(request, 'legendary/listings.html',context = context_dict)

    return response

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('legendary:index'))
