from django.db import models

class FiscalYear(models.Model):
    years = (
        ("2069", "2069/70"),
        ("2070", "2070/71"),
        ("2071", "2071/72")
    )
    year = models.IntegerField(choices=years)
