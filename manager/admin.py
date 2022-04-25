from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.RegistrationRequests)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'date_created', 'is_authenticated']
    list_editable = ['is_authenticated']
        
    def full_name(self, Registration):
        return Registration.first_name + " " + Registration.last_name
    