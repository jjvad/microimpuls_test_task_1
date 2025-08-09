from django.contrib import admin
from .models import PressureRecord

@admin.register(PressureRecord)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'systolic', 'diastolic', 'pulse', 'timestamp', 'notes')
