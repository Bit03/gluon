from django.db import models
from dapps.models import DApp

# Create your models here.


class Github(models.Model):
    dapp = models.ForeignKey(DApp, related_name='dapp')
    url = models.URLField(max_length=256, default='')



