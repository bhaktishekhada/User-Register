import self
from django.db import models
from django.contrib.auth.models import User
from django.template.backends import django
from django.db import models


# Create your models here.
# class Person(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     # birthday = models.DateField(null=True)
#     # gender = models.CharField(max_length=10)
#     # city = models.CharField(max_length=3)
#
#     def __str__(self):
#         return f"{self.username} {self.email} {self.password}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/',null=True)
    # video = models.FileField(upload_to='videos_uploaded', null=True)

    def __str__(self):
        # return f"{self.user} {self.birthdate} {self.gender} {self.city}"
        return self.user.username


