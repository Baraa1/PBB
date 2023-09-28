from django.db import models

class Document(models.Model):
    docfile              = models.FileField(upload_to='ImportFiles/%Y/%m/%d')
    accounts_file        = models.BooleanField(blank=True, null=True, default=False)
    locations_file       = models.BooleanField(blank=True, null=True, default=False)
    docking_records_file = models.BooleanField(blank=True, null=True, default=False)