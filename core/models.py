from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Cources(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    image_url = models.FileField(upload_to="cources/courceImage")
    price = models.IntegerField(validators=[MinValueValidator(1, "Price can't be negative.")])
    capacity = models.IntegerField(validators=[MinValueValidator(1, "Price can't be negative.")])
    syllabus = RichTextField()
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_listed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date_created']
        verbose_name_plural = 'Cources'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    fees_pending = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_authenticated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
    
    def username(self):
        return self.user.username
    
class EnrolledCources(models.Model):
    student = models.ForeignKey(to="Student", on_delete=models.CASCADE)
    cource = models.ForeignKey(to="Cources", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student.user.first_name + " - " + self.cource.title
    