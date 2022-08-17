from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    income = models.IntegerField(default=0)
    costum = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    markiting = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.name
