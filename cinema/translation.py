from modeltranslation.translator import register, TranslationOptions
from .models import Film, Cinema, Hall


@register(Film)
class FilmTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Cinema)
class CinemaTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'conditions')


@register(Hall)
class HallTranslationOptions(TranslationOptions):
    fields = ('name', 'description')