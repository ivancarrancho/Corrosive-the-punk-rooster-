from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from User.forms import RegistrationForm
from User.models import UserData
from .mixins import LoginRequiredMixin



def authentication(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'signup':
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/success-signup')

        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/success-loguin')

        elif action == 'logout':
            print 'hellow mtf'
            logout(request)
            return redirect('/success-logout')

    return render(request, 'login.html', {})

def create_data(request):
    if request.method == 'POST':
        myForm = RegistrationForm(request.POST)
        if myForm.is_valid():
            myForm.save()
            return redirect('/success-loguin')
    else:
        myForm = RegistrationForm()

    return render(request, 'user_form.html', {'myForm': myForm})

class UserPageView(ListView):
    model = UserData
    template_name = "user_list.html"

    def get_queryset(self):
        return User.objects.all()

class SuccessLoginView(LoginRequiredMixin, TemplateView):
    template_name = "success_login.html"

class SuccessSignUpView(TemplateView):
    template_name = "success_sign_up.html"

class SuccessLogoutView(TemplateView):
    template_name = "success_logout.html"
