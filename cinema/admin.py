from django.contrib import admin
from .models import Cinema, Film, Hall, Session


# Register your models here.
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_display_links = ('name',)


admin.site.register(Film, FilmAdmin)
admin.site.register(Cinema)
admin.site.register(Hall)
admin.site.register(Session)


# admin.site.register()
