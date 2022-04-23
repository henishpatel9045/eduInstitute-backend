from django.contrib import admin

from . import models


class CourceInline(admin.TabularInline):
    model = models.EnrolledCources
    fields = ['student', 'cource']
    min_num = 1
    extra = 0

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_per_page = 20
    search_fields = ['user__first_name', 'user__last_name']
    inlines = [CourceInline] 
    autocomplete_fields = ["user"]
    
    def full_name(self, student):
        return student.user.first_name + " " + student.user.last_name
    

@admin.register(models.Cources)
class CourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'capacity', 'price', 'is_listed']
    search_fields = ['title']
    