from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
