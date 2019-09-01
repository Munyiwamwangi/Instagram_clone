from django.contrib import admin
from .models import Article, Comment, Profile

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('comment',)

admin.site.register(Profile)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
