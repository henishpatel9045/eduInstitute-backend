from django.contrib import admin

from . import models

admin.site.site_header = "Admin"
admin.site.index_title = "Admin"

class StoryInline(admin.TabularInline):
    model = models.Story
    list_editable = ['is_listed']
    fields = ['sender_name', 'sender_email', 'date_created', 'is_listed']
    readonly_fields = ['sender_name', 'sender_email', 'date_created']
    extra = 0


@admin.register(models.SiteInfo)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_updated']
    inlines = [StoryInline]


@admin.register(models.Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['sender_name', 'sender_email', 'date_created', 'is_listed']
    list_editable = ['is_listed']    
    readonly_fields = ['sender_name', "sender_email", "content", "date_created"]

@admin.register(models.SocialMediaInfo)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ["id", "gmail", "last_updated"]
    
    
@admin.register(models.AddressInfo)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["id", "last_updated"]
    
    