from django.test import TestCase
from .models import Image, Profile, User

# Create your tests here.


class ImageTestClass(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username='user')
        self.image = Image(name="name", caption="me")

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)

    def test_delete_profile(self):
       self.new_image.delete_image()
       images = Image.objects.all()
       self.assertTrue(len(image) == 0)
