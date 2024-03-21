from django.contrib import admin

from apps.vacancy.models import Vacancy
# Register your models here.
@admin.register(Vacancy)
class Vacansy(admin.ModelAdmin):
    list_display = ('title', 'desc')
    search_fields = ('title', 'desc')
    list_filter = ('title',)