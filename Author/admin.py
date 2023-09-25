from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyAuthor

class MyAuthorAdmin(UserAdmin):
  form = UserChangeForm
  fieldsets = (
      (None, {'fields': ('username', 'password', )}),
      (_('Personal info'), {'fields': ('profile_pic','first_name', 'last_name')}),
      # (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
      #                                'groups', 'user_permissions')}),
      
        (_('user_info'), {'fields': ('bio','phone_no', 'email','address' )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('username', 'password1', 'password2'),
      }),
  )
  list_display = ['username','first_name', 'last_name', 'is_staff', "phone_no"]
  search_fields = ('first_name', 'last_name')
  readonly_fields = ['last_login', 'date_joined']
  
admin.site.register(MyAuthor, MyAuthorAdmin)

# admin.site.register(MyAuthor, MyAuthorAdmin)
