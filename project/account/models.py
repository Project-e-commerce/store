from django.db import models

class LogInView(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)




class registrationView(models.Model):
    email = models.EmailField(max_length=10)
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

class LogOutView(models.Model):
    success_message = 'Logout successfully'


