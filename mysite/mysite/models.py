from datetime import datetime
from django.conf import settings
from salesforce import models

"""
from mysite.models import Recordtype
Recordtype.objects.all().count()
"""


class Recordtype(models.Model):

    name = models.CharField(max_length=80)

    class Meta:
        app_label = 'salesforce'
        db_table = 'RecordType'
        verbose_name = 'Record Type'
        verbose_name_plural = 'Record Types'
