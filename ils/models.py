from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.conf.global_settings import LANGUAGES
from app.libr import unique_slugify


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=254, null=True, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')
    slug = models.SlugField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = u'Book Categories'


class Author(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(Author, self).save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=254)
    author = models.ForeignKey(Author)
    language = models.CharField(max_length=7, choices=LANGUAGES, default='en')
    category = models.ForeignKey(Category)
    slug = models.SlugField(max_length=255, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Book, self).save(*args, **kwargs)



