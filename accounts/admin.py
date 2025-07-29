
from django.contrib import admin
from .models import CustomUser, VoiceSample

admin.site.register(CustomUser)
admin.site.register(VoiceSample)

# Register your models here.
