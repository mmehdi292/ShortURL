
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UrlWithAccount)
admin.site.register(UrlWithoutAccount)
admin.site.register(User)