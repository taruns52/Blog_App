from django.db import models

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
