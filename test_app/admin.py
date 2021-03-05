from django.contrib import admin
from test_app.models import botwTest


# Register your models here.
class botwTestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_created', 'newsletter_campaign_id', 'newsletter_branding')


admin.site.register(botwTest, botwTestAdmin)