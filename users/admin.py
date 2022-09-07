from django.contrib import admin
from .models import User, Mail_template
# Register your models here.
admin.site.register(User)
admin.site.register(Mail_template)