from django.db import models
from datetime import datetime

# Create your models here.
class Cases(models.Model):
    path_to_file = models.CharField(max_length=100)
    classification = models.CharField(max_length=100, default='None')
    site = models.CharField(max_length=300)
    last_parsed = models.CharField(null=False, default=datetime.now().strftime("%m/%d/%Y"), max_length=150)


class ParsingStatus(models.Model):
    status = models.CharField(max_length=100, default='stopped')
    last_parsed = models.CharField(max_length=100, null=False, default=str(datetime.now().strftime("%m/%d/%Y")))
    site = models.CharField(max_length=300, null=False)