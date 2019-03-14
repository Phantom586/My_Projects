from django.db import models
from django.contrib.auth.models import User

#Create your models here.
class Register_User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    area = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.user.username} Profile'