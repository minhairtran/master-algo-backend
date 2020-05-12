from django.contrib import admin

# Register your models here.
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['content', 'user']
    search_fields = ['content', 'user__username']
    class Meta:
        model = Feedback

admin.site.register(Feedback, FeedbackAdmin)