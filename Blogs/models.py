from django.db import models
from django.urls import reverse

from Author.models import MyAuthor

# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(MyAuthor, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    author = models.ForeignKey(MyAuthor, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    commented_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-commented_on"]

    def __str__(self):
        return self.comment
