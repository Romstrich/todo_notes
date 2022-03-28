from django.db import models

# Create your models here.

class Author(models.Model):
    first_name=models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthdate = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Biography(models.Model):

    text=models.TextField(null=True,blank=True)
    author=models.OneToOneField(Author,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author)

class Book(models.Model):
    name=models.CharField(max_length=128)
    authors=models.ManyToManyField(Author)

    def __str__(self):
        return f'self.name'
