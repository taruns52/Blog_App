from django.urls import path
from .views import BlogList, BlogDetailView, BlogCreateView, MyBlogList

# from .views import

urlpatterns = [
    path("create-blog/", BlogCreateView.as_view(), name="create-blog"),
    path("my-blogs/", MyBlogList.as_view(), name="my-blogs"),
    path("", BlogList.as_view(), name="home"),
    path("<pk>/", BlogDetailView.as_view(), name="blog-detail"),
]
