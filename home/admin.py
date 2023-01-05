from django.contrib import admin
from home.models import Contact, logIn, logInsignup

# Register your models here.
admin.site.register(Contact)
admin.site.register(logIn)
admin.site.register(logInsignup)