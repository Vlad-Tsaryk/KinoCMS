from django.contrib import admin
from .models import Film,Cinema


# Register your models here.
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_display_links = ('name',)


admin.site.register(Film, FilmAdmin)
admin.site.register(Cinema)

# admin.site.register()
