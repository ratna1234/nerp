from django.db import models
from core.models import FiscalYear, Donor, Activity, Account, Budget, TaxScheme


class JournalVoucher(models.Model):
    fiscal_year = models.ForeignKey(FiscalYear)
    voucher_no = models.PositiveIntegerField()
    date = models.DateField()


class JournalVoucherRow(models.Model):
    account = models.ForeignKey(Account)
    dr_amount = models.PositiveIntegerField(blank=True, null=True)
    cr_amount = models.PositiveIntegerField(blank=True, null=True)


class Receipt(models.Model):
    date = models.DateField()
    no = models.PositiveIntegerField()
    fiscal_year = models.ForeignKey(FiscalYear)


class ReceiptRow(models.Model):
    sn = models.PositiveIntegerField()
    budget_head = models.ForeignKey(Budget)
    account = models.ForeignKey(Account)
    invoice_no = models.PositiveIntegerField(blank=True, null=True)
    # amount = models.FloatField()
    vattable = models.BooleanField(default=False)

    nepal_government = models.FloatField(blank=True, null=True)
    foreign_cash_grant = models.FloatField(blank=True, null=True)
    foreign_compensating_grant = models.FloatField(blank=True, null=True)
    foreign_cash_loan = models.FloatField(blank=True, null=True)
    foreign_compensating_loan = models.FloatField(blank=True, null=True)
    foreign_substantial_aid = models.FloatField(blank=True, null=True)

    donor = models.ForeignKey(Donor, blank=True, null=True)

    advanced = models.FloatField(blank=True, null=True)
    advanced_settlement = models.FloatField(blank=True, null=True)
    cash_returned = models.FloatField(blank=True, null=True)

    tax_scheme = models.ForeignKey(TaxScheme)
    activity = models.ForeignKey(Activity, blank=True, null=True)
    remarks = models.CharField(max_length=254, blank=True, null=True)

    receipt = models.ForeignKey(Receipt, related_name='rows')