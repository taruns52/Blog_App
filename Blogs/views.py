from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Blog

# Create your views here.


class BlogList(ListView):
    model = Blog
    context_object_name = "Blogs"
    paginate_by = 5


class BlogDetail(DetailView):
    model = Blog
