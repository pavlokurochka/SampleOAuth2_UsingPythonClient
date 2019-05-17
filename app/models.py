from django.db import models

# Create your models here.

class Token(models.Model):
    access_token = models.CharField('access token', max_length=2000)
    refresh_token = models.CharField('refresh token', max_length=200)
    realm_id = models.CharField('realm_id', max_length = 60)
    # description = models.TextField(blank=True)
    # event_date = models.DateTimeField('Event Date')
   