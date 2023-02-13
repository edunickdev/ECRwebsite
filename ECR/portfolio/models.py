from django.db import models


# Create your models here.
class Languages(models.Model):
    language = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.language


class Alternative_Tech(models.Model):
    Tech = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.Tech


class States(models.Model):
    category = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.category


class Portfolio(models.Model):
    id_language = models.ForeignKey('Languages', on_delete=models.CASCADE)
    id_state = models.ForeignKey('States', on_delete=models.CASCADE)
    id_alter_tech = models.ForeignKey('Alternative_Tech', on_delete=models.CASCADE)
