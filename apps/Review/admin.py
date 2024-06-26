from django.contrib import admin

from apps.Review.models import Review
from modeltranslation.admin import TranslationAdmin

class ReviewAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('name_ru', 'discription_ru', 'photo' ,'jobtitle_ru' )}),
        (u'Ky', {'fields': ('name_ky', 'discription_ky',  'jobtitle_ky')})
    ]

admin.site.register(Review, ReviewAdmin)