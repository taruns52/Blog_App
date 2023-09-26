from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.db.models import Count

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View

from django.contrib.auth import login, authenticate, logout

from Author.models import MyAuthor
from Blogs.models import Blog
from BlogApp import settings

from .forms import AddAuthorForm
from Author import forms


# Create your views here.
class Register(CreateView):
    form_class = AddAuthorForm
    template_name = "authentication/register.html"
    success_url = reverse_lazy("login")


class LoginView(View):
    template_name = "authentication/login.html"
    form_class = forms.LoginForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        form = self.form_class()
        message = "Please Login"
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print("form", request.POST)
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            print(user)
            if user is not None:
                login(request, user)
                print("Login Success")
                return redirect("home")
        message = "Login failed!"
        print("Login failed!")
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )


class LogoutView(View):
    def get(self, request):
        logout(request)
        print("User Logout Success")
        return redirect(settings.LOGIN_URL)


class AuthorList(ListView):
    context_object_name = "Authors"
    template_name = "author/myauthor_list.html"

    def get_queryset(self):
        queryset = MyAuthor.objects.all()[::-1]
        print("\n\n\n\n", queryset)
        return queryset


class AuthorDetail(DetailView):
    model = MyAuthor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = get_object_or_404(MyAuthor, pk=self.kwargs["pk"])
        context["blog_list"] = Blog.objects.filter(author=author.pk)
        return context
