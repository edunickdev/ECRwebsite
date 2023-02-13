from django.db import models


# Create your models here.
class Level_education(models.Model):
    level_education = models.CharField(max_length=40, null=False)


class Education(models.Model):
    id_level_education = models.ForeignKey(Level_education, on_delete=models.CASCADE)
    institution = models.CharField(max_length=40, null=False)
    title = models.CharField(max_length=30, null=False)

