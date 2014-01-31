from django.db import models

class Party(models.Model):
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254, blank=True, null=True)
    phone_no = models.CharField(max_length=100, blank=True, null=True)
    pan_no = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class FiscalYear(models.Model):
    years = (
        (2069, "2069/70"),
        (2070, "2070/71"),
        (2071, "2071/72")
    )
    year = models.IntegerField(choices=years)

    def __str__(self):
        return str(self.year) + '/' + str(self.year - 1999)


class AppSetting(models.Model):
    app_name = models.CharField(max_length=254)
    fiscal_year = models.ForeignKey(FiscalYear)
    header_for_forms = models.TextField()

    def __str__(self):
        return 'Default Settings ' + str(self.id)
