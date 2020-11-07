from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'LOGIN'
    }
    return render(request, 'login.html', context)

def signup(request):
    context = {
        'title': 'SIGNUP'
    }
    return render(request, 'signup.html', context)