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


class BlogDetailView(UpdateView):
    form_class = CommentCreateForm
    model = Blog
    template_name = "blogs/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentCreateForm
        comments = Comment.objects.filter(blog=self.kwargs["pk"])
        context["comments"] = comments
        context["count"] = comments.count()
        return context

    def form_valid(self, form):
        comment = form.cleaned_data.get("comment")
        new_comment, created = Comment.objects.get_or_create(
            author=self.request.user,
            blog=Blog.objects.get(pk=self.kwargs["pk"]),
            comment=comment,
        )
        return super(BlogDetailView, self).form_valid(form)


class MyBlogList(ListView):
    model = Blog
    context_object_name = "Blogs"
    template_name = "blogs/my_blog_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user.pk)
