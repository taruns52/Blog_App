from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import MyAuthor, Blog


class BlogInline(admin.TabularInline):
    model = Blog

    def has_change_permission(self, request, obj):
        return False


class MyAuthorAdmin(UserAdmin):
    inlines = [
        BlogInline,
    ]
    form = UserChangeForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (_("Personal info"), {"fields": ("profile_pic", "first_name", "last_name")}),
        (_("user_info"), {"fields": ("bio", "phone_no", "email", "address")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_display = ["username", "first_name", "last_name", "is_staff", "phone_no"]
    search_fields = ("first_name", "last_name")
    readonly_fields = ["last_login", "date_joined"]


admin.site.register(MyAuthor, MyAuthorAdmin)
