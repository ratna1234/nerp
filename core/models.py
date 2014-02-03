from django.db import models

from app.libr import MultiNameModel

SOURCES = [('nepal_government', 'Nepal Government'), ('foreign_cash_grant', 'Foreign Cash Grant'),
           ('foreign_compensating_grant', 'Foreign Compensating Grant'), ('foreign_cash_loan', 'Foreign Cash Loan'),
           ('foreign_compensating_loan', 'Foreign Compensating Loan'),
           ('foreign_substantial_aid', 'Foreign Substantial Aid')]


class Account(MultiNameModel):
    # account_page_no = models.IntegerField()
    pass


class Party(MultiNameModel):
    address = models.CharField(max_length=254, blank=True, null=True)
    phone_no = models.CharField(max_length=100, blank=True, null=True)
    pan_no = models.CharField(max_length=50, blank=True, null=True)
    account = models.OneToOneField(Account, related_name='party')

    def save(self, *args, **kwargs):
        if self.pk is None:
            account = Account(name_en=self.name_en, name_ne=self.name_ne)
            account.save()
            self.account = account
        super(Party, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Parties'


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


class Employee(MultiNameModel):
    pass

    def save(self, *args, **kwargs):
        if self.pk is None:
            account = Account(name_en=self.name_en, name_ne=self.name_ne)
            account.save()
            self.account = account
        super(Employee, self).save(*args, **kwargs)


class Donor(MultiNameModel):
    pass


class Activity(MultiNameModel):
    no = models.PositiveIntegerField()

    def __str__(self):
        return str(self.no) + ' - ' + self.name

    class Meta:
        verbose_name_plural = 'Activities'


class Budget(MultiNameModel):
    no = models.PositiveIntegerField()
    nepal_government = models.FloatField(default=0)
    foreign_cash_grant = models.FloatField(default=0)
    foreign_compensating_grant = models.FloatField(default=0)
    foreign_cash_loan = models.FloatField(default=0)
    foreign_compensating_loan = models.FloatField(default=0)
    foreign_substantial_aid = models.FloatField(default=0)

    def total(self):
        return self.nepal_government + self.foreign_cash_grant + self.foreign_compensating_grant + self.foreign_cash_loan + self.foreign_compensating_loan + self.foreign_substantial_aid


    def __str__(self):
        return str(self.no) + ' - ' + self.name + ' (' + str(self.total()) + ')'

    class Meta:
        verbose_name = 'Budget Head'