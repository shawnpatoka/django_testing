from django import forms
from django.forms import ModelForm
from .models import botwTest

class botwTestForm(ModelForm):
    class Meta:
        model = botwTest
        fields = ['newsletter_campaign_id','tile_1_location', 'tile_1_headline', 'tile_2_location', 'tile_2_headline', ]