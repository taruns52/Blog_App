from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from Blogs.forms import BlogCreateForm, CommentCreateForm

from .models import Blog, Comment

# Create your views here.


class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogCreateForm
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogCreateView, self).form_valid(form)


class BlogList(ListView):
    model = Blog
    context_object_name = "Blogs"
    paginate_by = 5


class BlogDetail(DetailView):
    model = Blog


class MyBlogList(ListView):
    model = Blog
    context_object_name = "Blogs"
    template_name = "blogs/my_blog_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user.pk)
