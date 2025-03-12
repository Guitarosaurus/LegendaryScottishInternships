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

    context_dict = {}
    response = render(request, 'legendary/update_profile_form.html', context=context_dict)

    return response

@login_required
def update_user_checklist(request):

    context_dict = {}
    response = render(request, 'legendary/update_user_checklist_form.html', context=context_dict)

    return response

def login(request):

    context_dict = {}
    response = render(request, 'legendary/login.html', context=context_dict)

    return response

def register(request):

    context_dict = {}
    response = render(request, 'legendary/register.html', context=context_dict)

    return response

def listings(request):

    context_dict = {}
    response = render(request, 'legendary/listings.html',context = context_dict)

    return response