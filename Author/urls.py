from django.urls import path, include
from .views import Register, LoginView, LogoutView, AuthorDetail, AuthorList

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("authors/", AuthorList.as_view(), name="authors"),
    path("<pk>/", AuthorDetail.as_view(), name="author-detail"),
]
