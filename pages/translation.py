from modeltranslation.translator import register, TranslationOptions
from .models import Main_page, Other_page, News_promo, Contact_page


@register(Main_page)
class Main_pageTranslationOptions(TranslationOptions):
    fields = ('seo_text',)


@register(Other_page)
class Other_pageTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(News_promo)
class News_promoTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Contact_page)
class Contact_pageTranslationOptions(TranslationOptions):
    fields = ('name', 'address')
