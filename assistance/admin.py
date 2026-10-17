from django.contrib import admin
from assistance.models import HelpRequest
# Register your models here.

@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ['rider', 'title', 'urgency']
    list_filter = ['rider', 'title', 'urgency']
    search_fields = ['rider', 'title', 'urgency']
