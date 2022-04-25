from core.models import Student
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models, transaction


# Create your models here.
class RegistrationRequests(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100, validators=[MinLengthValidator(8, "Password must be minimum of 8 charachters long.")])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    is_authenticated = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if self.is_authenticated:
            user = get_user_model().objects.filter(username=self.username).exists()
            if user:
                print("User with username " + self.username + " alredy exists.")
            else:
                with transaction.atomic():  
                    user = User.objects.create_user(self.username, self.email, self.password)
                    user.first_name = self.first_name
                    user.last_name = self.last_name                
                    user.save()
                    student = Student.objects.create(user=user, is_authenticated=self.is_authenticated)
                    student.save()

                print("User with username " + self.username + " created succefully.")
        super(RegistrationRequests, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Registration Requests'
