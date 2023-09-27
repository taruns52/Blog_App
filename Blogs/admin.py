from django.contrib import admin

from Blogs.models import Blog,Comment

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

    def has_change_permission(self, request, obj):
        return False

class BlogAdmin(admin.ModelAdmin):
    inlines = [
    CommentInline,
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "blog", "get_comment", "commented_on"]

    def get_comment(self, obj):
        return obj.comment[:25]

    get_comment.short_description = "Comments"




admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
