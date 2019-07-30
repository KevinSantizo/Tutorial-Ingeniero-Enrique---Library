from django.db import models
from users.models import User
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    publication_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.name + ' (' + self.author.first_name + ' ' + self.author.last_name + ')'
