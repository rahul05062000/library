from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20,primary_key=True)
    category = models.CharField(max_length=100)