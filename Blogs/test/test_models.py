from django.test import TestCase

from Author.models import MyAuthor
from Blogs.models import Blog


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MyAuthor.objects.create(
            username="zxcvb",
            first_name="Ramji",
            last_name="Raja",
            bio="I am Proud Author",
            phone_no="9632587410",
        )

        author = MyAuthor.objects.get(pk=1)

        Blog.objects.create(
            author=author,
            title="My life my Goals",
            content="Raja, I am Proud AuthorI am Proud AuthorI am Proud Author",
        )
        Blog.objects.create(
            author=author,
            title="My life ",
            content="Raja, I am Proud AuthorI am Proud AuthorI am Proud Author",
        )

    def test_correct_label_and_length(self):
        expected_fields = [
            {"name": "title", "max_length": 200},
        ]

        for field in expected_fields:
            model_field = Blog._meta.get_field(field["name"])
            self.assertEqual(model_field.verbose_name, field["name"])
            self.assertEqual(model_field.max_length, field["max_length"])

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.get_absolute_url(), "/1/")

    def test_correct_returned_str_value(self):
        blog = Blog.objects.get(pk=1)
        self.assertEqual(str(blog), blog.title)
