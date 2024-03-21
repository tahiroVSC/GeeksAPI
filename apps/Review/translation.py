from modeltranslation.translator import translator, TranslationOptions
from apps.Review.models import Review

class ReviewTranslationOptions(TranslationOptions):
    fields = ('name', 'discription', 'jobtitle')

translator.register(Review, ReviewTranslationOptions)