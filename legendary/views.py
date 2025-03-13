from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from legendary.forms import UserForm,UserProfileForm,CompanyForm,InternshipForm,CommentForm,ChangeChecklistForm
from legendary.models import Company, Internship, Comment, UserProfile
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime



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

def report(request):

    context_dict = {}
    response = render(request,'legendary/reportform.html', context = context_dict)

    return response

def profile(request):

    context_dict = {}
    response = render(request, 'legendary/profile.html', context=context_dict)

    return response

@login_required
def update_profile(request):

    form = UserProfileForm()

    if form.is_valid():

        form.save(commit = True)

        return redirect('/legendary/')
    
    else:

        print(form.errors)


    response = render(request, 'legendary/update-profile.html', {'form': form})

    return response

@login_required
def change_checklist(request):
    form = ChangeChecklistForm()

    if form.is_valid():
        
        form.save(commit = True)
        #wondering the best redirect here
        return redirect('/legendary/')
    
    else:
        
        print(form.errors)   
    
    response = render(request, 'legendary/update-checklist.html', {'form': form})
    
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

def listings(request):

    context_dict = {}
    response = render(request, 'legendary/listings.html',context = context_dict)

    return response

