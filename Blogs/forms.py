
from django import forms
from Blogs.models import Blog,Comment


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title","content")



class CommentCreateForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols':100, 'placeholder':'Post Your Comment'}))
    class Meta:
        model = Comment
        fields = ("comment",)