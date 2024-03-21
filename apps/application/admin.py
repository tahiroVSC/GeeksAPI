from django.contrib import admin
from django.contrib.auth.models import User, Group
from apps.application.models import Application
# Register your models here.

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'number')
    search_fields = ('name', 'surname')
    list_filter = ('name', 'surname')
    
# admin.site.unregister(Group)
# admin.site.unregister(User)