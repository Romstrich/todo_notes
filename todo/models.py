from django.db import models

# Create your models here.
from users.models import User


class Project(models.Model):
    name=models.CharField(max_length=128)
    users=models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'

class Todo(models.Model):
    project=models.OneToOneField(Project,on_delete=models.CASCADE,unique=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_user=models.OneToOneField(User,on_delete=models.CASCADE,unique=False)
    active=models.BooleanField()
    note_text=models.TextField()