from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class SocialMediaInfo(models.Model):
    gmail = models.EmailField()
    facebook = models.URLField()
    whatsapp = models.URLField()
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkdln = models.URLField(null=True, blank=True)
    site = models.OneToOneField(to="SiteInfo", on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = 'SocialMediaInfo'
    
class AddressInfo(models.Model):
    address = RichTextField()
    google_map_location = models.URLField(null=True, blank=True)
    site = models.OneToOneField(to="SiteInfo", on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = "AddressInfo"
        

class Story(models.Model):
    sender_name = models.CharField(max_length=50)
    sender_email = models.EmailField(null=True, blank=True)
    sender_cource = models.CharField(max_length=100, null=True, blank=True)
    content = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_listed = models.BooleanField(default=False)
    site = models.ForeignKey(to="SiteInfo", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.sender_name

    class Meta:
        verbose_name_plural = "Stories"
        

class SiteInfo(models.Model):
    name = models.CharField(max_length=150) 
    owner = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    timings = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "SiteInfo"