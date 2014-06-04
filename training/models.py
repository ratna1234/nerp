from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=254, null=True, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')

    class Meta:
        verbose_name_plural = 'Categories'


class TargetGroup(MPTTModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=254, null=True, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')


class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)


class Participant(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_no = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(blank=True, null=True)


class ResourcePerson(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_no = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(blank=True, null=True)


class Training(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)
    starts = models.DateTimeField(blank=True, null=True)
    ends = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='trainings', blank=True, null=True)
    target_groups = models.ManyToManyField(TargetGroup, related_name='trainings', blank=True, null=True)
    criteria_for_selection = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    output = models.TextField(blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    curriculum = models.TextField(blank=True, null=True)
    resource_persons = models.ManyToManyField(ResourcePerson, related_name='trainings')
    participants = models.ManyToManyField(Participant, related_name='trainings')


class File(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True, upload_to='training/files/')
    training = models.ForeignKey(Training)