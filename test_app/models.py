from django.db import models

NEWSLETTER_BRANDING = (
    ('branding_botw','Best of the Week'),
    ('branding_bh','Gear Alert'),
)


class botwTest(models.Model):
    date_created 				= models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    newsletter_campaign_id  	= models.CharField(max_length=200, null=True)
    newsletter_branding		  	= models.CharField(max_length=25, choices=NEWSLETTER_BRANDING, default='custom_field')
    tile_1_location  			= models.CharField(max_length=200, null=True, blank=True)
    tile_1_headline             = models.CharField(max_length=200, null=True, blank=True)
    tile_2_location  			= models.CharField(max_length=200, null=True, blank=True)
    tile_2_headline             = models.CharField(max_length=200, null=True, blank=True)
    tile_3_location  			= models.CharField(max_length=200, null=True, blank=True)
    tile_3_headline             = models.CharField(max_length=200, null=True, blank=True)
    tile_4_location  			= models.CharField(max_length=200, null=True, blank=True)
    tile_4_headline             = models.CharField(max_length=200, null=True, blank=True)
    tile_5_location  			= models.CharField(max_length=200, null=True, blank=True)
    tile_5_headline             = models.CharField(max_length=200, null=True, blank=True)
    tile_6_location  			= models.CharField(max_length=200, null=True, blank=True)
    tile_6_headline             = models.CharField(max_length=200, null=True, blank=True)






    # video_include		= models.BooleanField(default=False, null=True, blank=False)


    class Meta:
        verbose_name = "Best of the Week Test"
        verbose_name_plural = 'Best of the Week Test'