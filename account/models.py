from django.db import models
from app.libr import MultiNameModel
from core.models import FiscalYear, Donor, Activity
from core.models import Budget


class Account(MultiNameModel):
    # name = models.CharField(max_length=100)
    account_page_no = models.IntegerField()


class JournalVoucher(models.Model):
    fiscal_year = models.ForeignKey(FiscalYear)
    voucher_no = models.PositiveIntegerField()
    date = models.DateField()


class JournalVoucherRow(models.Model):
    account = models.ForeignKey(Account)
    dr_amount = models.PositiveIntegerField(blank=True, null=True)
    cr_amount = models.PositiveIntegerField(blank=True, null=True)


# class Receipt(models.Model):
#     pass
#
#
# class ReceiptRow(models.Model):
#     sn = models.PositiveIntegerField()
#     budget = models.ForeignKey(Budget)
#     account = models.ForeignKey(Account)
#     invoice_no = models.PositiveIntegerField(blank=True, null=True)
#     amount = models.FloatField()
#     vattable = models.BooleanField(default=False)
#     sources = [('nepal_government', 'Nepal Government'), ('donor_organisation', 'Donor Organisation')]
#     source = models.CharField(choices=sources, max_length=50, default='nepal_government')
#     donor = models.ForeignKey(Donor, blank=True, null=True)
#     advanced = models.FloatField(blank=True, null=True)
#     advanced_fasrsyuat = models.FloatField(blank=True, null=True)
#     amount_returned = models.FloatField(blank=True, null=True)
#     activity = models.ForeignKey(Activity, blank=True, null=True)
#     remarks = models.CharField(max_length=254)