from django.db import models


# Create your models here.

class Network(models.Model):
    url = models.CharField(max_length=100, null=False)
    shortname = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.url


class About_me(models.Model):
    document = models.IntegerField(null=False, primary_key=True)
    names = models.CharField(max_length=35, null=False)
    last_names = models.CharField(max_length=35, null=False)
    address = models.CharField(max_length=40, null=False)
    networks = models.ForeignKey('Network', on_delete=models.CASCADE)

    def __str__(self):
        return self.names

