from django.contrib import admin

from .models import *

@admin.register(AnswerSheet)
class ProfileAdmin(admin.ModelAdmin):
    pass

