
from django.urls import path, include
from .views import Register, LoginPageView, Homepage

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('login/', LoginPageView.as_view(), name='login'),
    # path('admin/', admin.site.urls),
    path('', Homepage, name='home'),
] 
