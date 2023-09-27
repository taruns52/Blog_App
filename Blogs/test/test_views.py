from django.test import TestCase
from django.urls import reverse

from Author.models import MyAuthor
from Blogs.models import Blog


# Create your tests here.
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        total_Authors = 21

        for blog_id in range(total_Authors):
            MyAuthor.objects.create(
                username=f"author{blog_id}",
            )

            author = MyAuthor.objects.get(pk=1)
            Blog.objects.create(
                author=author,
                title=f"My Blog {blog_id}",
            )
       
    def test_all_blog_page_accessiblity(self):
        blog = self.client.get("/")
        self.assertEqual(blog.status_code, 200)

    def test_all_blog_page_accessiblity(self):
        # Here all blogs page is named in urlpatterns as home
        blog = self.client.get(reverse("home"))
        self.assertEqual(blog.status_code, 200)

    def test_all_blogs_page_uses_expected_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "Blogs/blog_list.html")

    def test_all_blogs_page_pagination(self):
        response = self.client.get("/")
        self.assertEqual(len(response.context["Blogs"]), 5)
