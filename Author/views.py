from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.views.generic import View

from django.contrib.auth import login, authenticate

from .forms import AddAuthorForm
from Author import forms

# Create your views here.
class Register(CreateView):
    form_class = AddAuthorForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy("login")

# class Create_Author(CreateView):
#     form_class = AddAuthorForm
#     template_name = 'add_author.html'
#     success_url = reverse_lazy("login")



class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm
    
    def get(self, request):
        form = self.form_class()
        message = 'Please Login'
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})
    
def Homepage(request):
    return render(request, 'blogs/homepage.html')