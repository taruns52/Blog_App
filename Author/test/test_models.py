from django.test import TestCase

from Author.models import MyAuthor
from Blogs.models import Blog

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        MyAuthor.objects.create(username='zxcvb',first_name='Ramji', last_name='Raja',bio='I am Proud Author', phone_no='9632587410')
        MyAuthor.objects.create(username='asdfg',first_name='Ramesh', last_name='Raja',bio='I am Proud Author', phone_no='9632587410')
        
    def test_correct_label_and_length(self):
        expected_fields = [
            {'name':'bio', 'max_length':100 },
            {'name':'address', 'max_length':100},
        ]

        for field in expected_fields:
            model_field = MyAuthor._meta.get_field(field['name'])
            self.assertEqual(model_field.verbose_name, field['name'])
            self.assertEqual(model_field.max_length, field['max_length'])

    def test_correct_returned_str_value(self):
        author = MyAuthor.objects.get(pk=1)
        self.assertEqual(str(author), author.username)
