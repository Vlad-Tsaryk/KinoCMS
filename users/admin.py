from django.contrib import admin
from .models import User, Mail_template, Ticket
# Register your models here.
admin.site.register(User)
admin.site.register(Mail_template)
admin.site.register(Ticket)