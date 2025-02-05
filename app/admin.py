from django.contrib import admin
from app.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    exclude = ('slug',)
    summernote_fields = ('title','cover','description','content',)  # Enable Summernote in admin

admin.site.register(Article, ArticleAdmin)
@admin.register(EmailSubmission)
class EmailSubmissionAdmin(admin.ModelAdmin):
    list_display = ('email', 'submitted_at')

# Register your models here.
