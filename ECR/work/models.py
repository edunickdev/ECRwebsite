from django.db import models

# Create your models here.
class Role(models.Model):
    level_role = models.CharField(max_length=40, null=False)
    description = models.TextField(max_length=280, null=False)


class Employee(models.Model):
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    enterprise = models.CharField(max_length=35, null=False)
    duration = models.CharField(max_length=30, null=False)
