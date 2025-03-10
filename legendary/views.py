from django.shortcuts import render

# Create your views here.
def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {}
    context_dict['boldmessage']= 'Crunchy, creamy, cookie, candy, cupcake!'
    
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

def update_profile(request):

    context_dict = {}
    response = render(request, 'legendary/update_profile_form.html', context=context_dict)

    return response

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