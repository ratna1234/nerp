from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from core.models import Language
from app.libr import unique_slugify
from users.models import User
import os
import datetime


class Subject(MPTTModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=254, null=True, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')
    slug = models.SlugField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(Subject, self).save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(Author, self).save(*args, **kwargs)


class Place(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(Place, self).save(*args, **kwargs)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(Publisher, self).save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254, null=True, blank=True)
    authors = models.ManyToManyField(Author, blank=True)
    languages = models.ManyToManyField(Language)
    subjects = models.ManyToManyField(Subject)
    slug = models.SlugField(max_length=255, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Book, self).save(*args, **kwargs)


class Record(models.Model):
    edition = models.CharField(max_length=254, null=True, blank=True)
    formats = (
        ('Paperback', 'Paperback'),
        ('Hardcover', 'Hardcover'),
        ('eBook', 'eBook')
    )
    format = models.CharField(max_length=10, default='Paperback', choices=formats)
    pagination = models.CharField(max_length=254, null=True, blank=True)
    isbn13 = models.CharField(max_length=254, null=True, blank=True)
    date_of_publication = models.DateField(null=True, blank=True)
    publication_has_month = models.BooleanField(default=True)
    publication_has_day = models.BooleanField(default=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True, default=1)
    types = (
        ('Reference', 'Reference'),
        ('Circulative', 'Circulative')
    )
    type = models.CharField(choices=types, max_length=11)
    book = models.ForeignKey(Book)
    openlibrary_url = models.URLField(blank=True, null=True)
    # thumbnail = models.ImageField(blank=True, null=True, upload_to='ils/thumbnails/')
    small_cover = models.ImageField(blank=True, null=True, upload_to='ils/covers/small/')
    medium_cover = models.ImageField(blank=True, null=True, upload_to='ils/covers/medium/')
    large_cover = models.ImageField(blank=True, null=True, upload_to='ils/covers/large/')
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    date_added = models.DateField()
    goodreads_id = models.PositiveIntegerField(null=True, blank=True)
    librarything_id = models.PositiveIntegerField(null=True, blank=True)
    openlibrary_id = models.CharField(max_length=254, null=True, blank=True)
    lcc = models.CharField(max_length=100, null=True, blank=True)
    ddc = models.CharField(max_length=100, null=True, blank=True)
    lccn_id = models.CharField(max_length=100, null=True, blank=True)
    oclc_id = models.CharField(max_length=100, null=True, blank=True)
    published_places = models.ManyToManyField(Place)
    weight = models.CharField(max_length=254, null=True, blank=True)
    dimensions = models.CharField(max_length=254, null=True, blank=True)
    by_statement = models.CharField(max_length=254, null=True, blank=True)
    notes = models.CharField(max_length=254, null=True, blank=True)
    excerpt = models.CharField(max_length=254, null=True, blank=True)

    def __unicode__(self):
        title = self.book.title
        if self.edition:
            title = title + ' (' + self.edition + ')'
        if self.format != 'Paperback':
            title = title + ' [' + self.format + ']'
        return title

    def ebooks(self, book_format=None):
        ebooks = BookFile.objects.filter(record=self)
        if book_format:
            books = []
            for ebook in ebooks:
                if ebook.format == book_format:
                    books.append(ebook)
            return books
        else:
            return ebooks

    def published_date(self):
        if self.publication_has_day:
            return self.date_of_publication
        elif self.publication_has_month:
            return self.date_of_publication.strftime('%B %Y')


class BookFile(models.Model):
    file = models.FileField(upload_to='ils/books/')
    record = models.ForeignKey(Record, related_name='files')

    def format(self):
        filename = self.file.file.name
        ext = os.path.splitext(filename)[1]
        if ext[0] == '.':
            ext = ext[1:]
        if ext == 'txt':
            return 'text'
        return ext

    format = property(format)

    def __unicode__(self):
        return unicode(self.record) + ' {' + self.format + '}'


class Transaction(models.Model):
    record = models.ForeignKey(Record)
    user = models.ForeignKey(User, related_name='transactions')
    borrow_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)
    fine_per_day = models.FloatField()
    fine_paid = models.FloatField(default=False)

    @staticmethod
    def new():
        transaction = Transaction()
        transaction.borrow_date = datetime.datetime.today()
        from ils.models import LibrarySetting

        setting = LibrarySetting.get()
        transaction.due_date = transaction.borrow_date + datetime.timedelta(days=setting.borrow_days)
        transaction.fine_per_day = setting.fine_per_day
        return transaction


class LibrarySetting(models.Model):
    fine_per_day = models.FloatField()
    borrow_days = models.PositiveIntegerField()
    types = (
        ('Reference', 'Reference'),
        ('Circulative', 'Circulative')
    )
    default_type = models.CharField(choices=types, unique=True, max_length=11, default='circulative')

    @staticmethod
    def get():
        return LibrarySetting.objects.all()[0]


def not_returned(self):
    transactions = Transaction.objects.filter(user=self, return_date=None)
    return transactions


def past_due(self):
    transactions = Transaction.objects.filter(user=self, return_date=None, due_date__lt=datetime.datetime.today())
    return transactions


User.add_to_class('not_returned', not_returned)
User.add_to_class('past_due', past_due)

