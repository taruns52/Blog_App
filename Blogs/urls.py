from django.urls import path
from .views import BlogList, BlogDetail

# from .views import

urlpatterns = [
    path("", BlogList.as_view(), name="home"),
    path("<pk>/", BlogDetail.as_view(), name="blog-detail"),
]
