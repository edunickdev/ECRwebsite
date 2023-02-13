from django.db import models


# Create your models here.
class About_me(models.Model):
    document = models.IntegerField(max_length=12, null=False, primary_key=True)
    names = models.CharField(max_length=35, null=False)
    last_names = models.CharField(max_length=35, null=False)
    address = models.CharField(max_length=40, null=False)
    networks = models.CharField(max_length=250, null=False)