from django.contrib.auth.models import User
from django.db import models
import datetime as dt

# Create your models here.    
class Comment(models.Model):
    comment=models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Profile(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=60)
    bio = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_article(self):
        self.save()

    def delete_Article(self):
        self.delete()

    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
