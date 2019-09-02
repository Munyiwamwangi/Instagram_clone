from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    picture = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    comments = models.TextField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
        

class Profile(models.Model):
    infor = models.IntegerField(default=0)
    name=models.CharField( max_length=50, default='Anonym')
    bio = models.CharField(max_length=80 , blank=True)
    profile_picture = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        ordering = ['profile_picture']

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    name = models.CharField(max_length=70)
    profile = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    caption = models.TextField()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        images = cls.objects.filter(image__name__icontains=search_term)
        return images

