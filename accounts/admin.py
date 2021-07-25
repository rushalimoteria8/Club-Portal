from django.contrib import admin
from accounts.models import add_event

# Register your models here.

from .models import *
# admin.site.register(Participants)
# admin.site.register(Club)
# admin.site.register(participates)
    
admin.site.register(add_event)