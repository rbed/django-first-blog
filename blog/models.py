from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Article(models.Model):
    meta_title = models.CharField(max_length=70)
    meta_desc = models.CharField(max_length=170)
    title = models.CharField(max_length=250)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    create_date = models.DateField(default=timezone.now)
    pub_date = models.DateField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default='admin')


    def publish(self):
        self.pub_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title





