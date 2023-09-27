
from django import forms
from Blogs.models import Blog


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title","content")