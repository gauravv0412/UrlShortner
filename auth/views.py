from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate

from auth.forms import Loginform

# Create your views here.

class Login(LoginView):
    template_name = 'auth/login.html'
    # authentication_form = Loginform

class Logout(LogoutView):
    template_name = 'auth/login.html'

class Myexception(Exception):
    def __init__(self, error_list):
        self.error_list = error_list

def signup(request):
    error = ""
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        e1 = ''
        e2 = ''
        e3 = ''
        try:
            if username == '':
                e1 = 'Username is necessory'
            if email == '':
                e2 = 'Email is necessory'
            if password == '':
                e3 = 'Password is necessory'
            if e1 != '' or e2 != '' or e3 != '':
                error = [e1, e2, e3]
                raise Myexecption(error)
            User.objects.get(username=username)
        except Myexception as err:
            context = {
                "error1": err.error_list[0],
                "error2": err.error_list[1],
                "error3": err.error_list[2]
            }
            return render(request, 'auth/signup.html', context)
        except:
            user = User.objects.create_user(username, email, password)
            user.save()
            return render(request, 'auth/afterSignup.html')
        error = "Username already exists"
        context = {
            "error": error
        }
        return render(request, 'auth/signup.html', context)
    else:
        return render(request, 'auth/signup.html')
