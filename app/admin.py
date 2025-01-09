from django.contrib import admin
from app.models import *

@admin.register(EmailSubmission)
class EmailSubmissionAdmin(admin.ModelAdmin):
    list_display = ('email', 'submitted_at')

# Register your models here.
