# need to add from.models and register(Sticky)

from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Sticky)               

admin.site.register(Sticky2)
# Sticky is the model name