from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from app.libr import title_case
from core.models import Language
from ils.forms import RecordForm, OutgoingForm, IncomingForm
from ils.models import LibrarySetting
from ils.serializers import RecordSerializer, AuthorSerializer, PublisherSerializer, SubjectSerializer, BookSerializer, TransactionSerializer
import isbn as isbnpy
import urllib2, urllib
import json
import pprint
from models import Record, Author, Publisher, Book, Subject, Place, BookFile, Transaction
import os
from django.core.files import File
from datetime import datetime
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from users.models import User

pp = pprint.PrettyPrinter(indent=4).pprint


@login_required
def authors_as_json(request):
    items = Author.objects.all()
    items_data = AuthorSerializer(items).data
    return HttpResponse(json.dumps(items_data), mimetype="application/json")


@login_required
def publishers_as_json(request):
    items = Publisher.objects.all()
    items_data = PublisherSerializer(items).data
    return HttpResponse(json.dumps(items_data), mimetype="application/json")


@login_required
def subjects_as_json(request):
    items = Subject.objects.all()
    items_data = SubjectSerializer(items).data
    return HttpResponse(json.dumps(items_data), mimetype="application/json")


@login_required
def books_as_json(request):
    items = Book.objects.all()
    items_data = BookSerializer(items).data
    return HttpResponse(json.dumps(items_data), mimetype="application/json")


# Create your views here.
def acquisition(request):
    record_data = {}
    record = None
    if request.GET.get('isbn'):
        isbn = request.GET.get('isbn')
        if isbnpy.isValid(isbn):
            # response = urllib2.urlopen('http://openlibrary.org/api/volumes/brief/json/isbn:' + isbn)
            response = urllib2.urlopen('http://127.0.0.1/json/3.json')
            data = json.load(response)
            data = data.itervalues().next()['records'].itervalues().next()
            if isbnpy.isI10(isbn):
                isbn = isbnpy.convert(isbn)
            try:
                record = Record.objects.get(isbn13=isbn)
                new_record = False
            except Record.DoesNotExist:
                record = Record(isbn13=isbn)
                new_record = True
                # pp(data)
            if record.book_id:
                book = record.book
            else:
                book = Book()
            book.title = data['data']['title']
            if data['details']['details'].has_key('subtitle'):
                book.subtitle = data['details']['details']['subtitle']
            book.save()

            if data['details']['details'].has_key('pagination'):
                record.pagination = data['data']['pagination']
            elif data['details']['details'].has_key('number_of_pages'):
                record.pagination = str(data['data']['number_of_pages']) + ' p.'

            if data['details']['details'].has_key('physical_format'):
                record.format = data['details']['details']['physical_format']
                if record.format.startswith('electronic'):
                    record.format = 'eBook'
                # record.openlibrary_url = data['data']['url']

            if data['details']['details'].has_key('weight'):
                record.weight = data['details']['details'].get('weight')
            if data['details']['details'].has_key('physical_dimensions'):
                record.dimensions = data['details']['details'].get('physical_dimensions')

            if data['data'].has_key('classifications'):
                if data['data']['classifications'].has_key('dewey_decimal_class'):
                    record.ddc = data['data']['classifications'].get('dewey_decimal_class')[0]
                if data['data']['classifications'].has_key('lc_classifications'):
                    record.lcc = data['data']['classifications'].get('lc_classifications')[0]

            try:
                record.date_of_publication = datetime.strptime(data['data']['publish_date'], '%B %d, %Y').date()
                record.publication_has_month = True
                record.publication_has_day = True
            except ValueError:
                try:
                    record.date_of_publication = datetime.strptime(data['data']['publish_date'], '%Y').date()
                    record.publication_has_month = False
                    record.publication_has_day = False
                except ValueError:
                    record.date_of_publication = datetime.strptime(data['data']['publish_date'], '%B %Y').date()
                    record.publication_has_day = False
                    record.publication_has_month = True

            if data['data'].has_key('identifiers'):
                if data['data']['identifiers'].has_key('openlibrary'):
                    record.openlibrary_id = data['data']['identifiers']['openlibrary'][0]
                if data['data']['identifiers'].has_key('goodreads'):
                    record.goodreads_id = data['data']['identifiers']['goodreads'][0]
                if data['data']['identifiers'].has_key('librarything'):
                    record.librarything_id = data['data']['identifiers']['librarything'][0]
                if data['data']['identifiers'].has_key('oclc'):
                    record.oclc_id = data['data']['identifiers']['oclc'][0]
                if data['data']['identifiers'].has_key('lccn'):
                    record.lccn_id = data['data']['identifiers']['lccn'][0]

            if data['data'].has_key('by_statement'):
                record.by_statement = data['data'].get('by_statement')

            if data['data'].has_key('notes'):
                record.notes = data['data'].get('notes')

            if data['data'].has_key('excerpts'):
                record.excerpt = data['data'].get('excerpts')[0].get('text')

            record.book = book

            setting = LibrarySetting.get()
            record.type = setting.default_type

            if new_record:
                record.date_added = datetime.today()
            record.save()

            if data['details']['details'].has_key('languages'):
                record.languages.clear()
                for lang in data['details']['details']['languages']:
                    lang_key = lang['key'].replace('/languages/', '')
                    try:
                        book_lang = Language.objects.get(code=lang_key)
                    except Language.DoesNotExist:
                        try:
                            book_lang = Language.objects.get(code=lang_key[:-1])
                        except Language.DoesNotExist:
                            raise Exception(
                                "Please add a language with code " + lang_key + " or " + lang_key[:-1] + " first!")
                    record.languages.add(book_lang)

            if data['data'].has_key('publish_places'):
                record.published_places.clear()
                for place in data['data']['publish_places']:
                    try:
                        published_place = Place.objects.get(name=place['name'])
                    except Place.DoesNotExist:
                        published_place = Place(name=place['name'])
                    published_place.save()
                    record.published_places.add(published_place)

            record.authors.clear()
            for author in data['details']['details']['authors']:
                author_key = author['key'].replace('/authors/', '')
                try:
                    book_author = Author.objects.get(identifier=author_key)
                except Author.DoesNotExist:
                    book_author = Author(identifier=author_key)
                book_author.name = author['name']
                book_author.save()
                record.authors.add(book_author)

            if data['data'].has_key('ebooks'):
                if data['data']['ebooks'][0].has_key('formats'):
                    formats = data['data']['ebooks'][0]['formats']
                    for book_format in formats:
                        ebooks = record.ebooks(book_format)
                        for ebook in ebooks:
                            ebook.delete()
                        if formats[book_format].has_key('url'):
                            url = formats[book_format].get('url')
                            result = urllib.urlretrieve(url)
                            book_file = BookFile(record=record)
                            book_file.file.save(
                                os.path.basename(url),
                                File(open(result[0]))
                            )
                            book_file.save()

            subjects = None
            if data['details']['details'].has_key('subjects'):
                subjects = data['details']['details']['subjects']
            elif data['data'].has_key('subjects'):
                subjects = data['data']['subjects']
            if subjects:
                record.book.subjects.clear()
                for subject in subjects:
                    if type(subject) == dict:
                        subject = title_case(subject['name'])
                    try:
                        book_subject = Subject.objects.get(name=subject)
                    except Subject.DoesNotExist:
                        book_subject = Subject(name=subject)
                    book_subject.save()
                    record.book.subjects.add(book_subject)

            # record.publishers.clear()
            # for publisher in data['details']['details']['publishers']:
            #     try:
            #         book_publisher = Publisher.objects.get(name=publisher['name'])
            #     except Publisher.DoesNotExist:
            #         book_publisher = Publisher(name=publisher['name'])
            #         book_publisher.save()
            #     record.publishers.add(book_publisher)
            try:
                book_publisher = Publisher.objects.get(name=data['details']['details']['publishers'][0])
            except Publisher.DoesNotExist:
                book_publisher = Publisher(name=data['details']['details']['publishers'][0])
                book_publisher.save()
            record.publisher = book_publisher

            cover_url = data['data']['cover']['large']
            result = urllib.urlretrieve(cover_url)
            record.large_cover.save(
                os.path.basename(cover_url),
                File(open(result[0]))
            )
            cover_url = data['data']['cover']['medium']
            result = urllib.urlretrieve(cover_url)
            record.medium_cover.save(
                os.path.basename(cover_url),
                File(open(result[0]))
            )
            cover_url = data['data']['cover']['small']
            result = urllib.urlretrieve(cover_url)
            record.small_cover.save(
                os.path.basename(cover_url),
                File(open(result[0]))
            )



            # thumbnail_url = data['details']['thumbnail_url']
            # result = urllib.urlretrieve(thumbnail_url)
            # record.thumbnail.save(
            #     os.path.basename(thumbnail_url),
            #     File(open(result[0]))
            # )

            # import pdb
            #
            # pdb.set_trace()
            record_data = RecordSerializer(record).data

    record_form = RecordForm(instance=record)

    return render(request, 'acquisition.html', {'data': record_data, 'form': record_form})


def save_acquisition(request):
    if request.POST.get('book').isnumeric():
        book = Book.objects.get(id=request.POST.get('book'))
        new_book = False
    else:
        book = Book(title=request.POST.get('book'))
        book.save()
        new_book = True

    if request.POST.get('isbn'):
        isbn = request.POST.get('isbn')
        if isbnpy.isValid(isbn):
            if isbnpy.isI10(isbn):
                isbn = isbnpy.convert(isbn)
            try:
                record = Record.objects.get(isbn13=isbn)
                new_record = False
            except Record.DoesNotExist:
                record = Record(isbn13=isbn)
                new_record = True
    else:
        if not new_book:
            try:
                record = Record.objects.get(book=book, edition=request.POST.get('book'))
                new_record = False
            except Record.DoesNotExist:
                record = Record(book=book)
                new_record = True
        else:
            record = Record(book=book)
            new_record = True

    record.book = book
    record.format = request.POST.get('format')
    if record.format != 'ebook':
        if new_record:
            record.quantity = request.POST.get('quantity')
        else:
            record.quantity += int(request.POST.get('quantity'))

    book.subtitle = request.POST.get('subtitle')
    record.excerpt = request.POST.get('excerpt')
    record.edition = request.POST.get('edition')
    record.notes = request.POST.get('notes')
    record.ddc = request.POST.get('ddc')
    record.lcc = request.POST.get('lcc')
    record.pagination = request.POST.get('pagination')
    record.format = request.POST.get('format')
    record.type = request.POST.get('type')
    if record.format != 'eBook':
        record.quantity = request.POST.get('quantity')

    record.publication_has_month = False
    record.publication_has_day = False
    if request.POST.get('year'):
        dt = datetime(int(request.POST.get('year')), 1, 1)
        if request.POST.get('month'):
            record.publication_has_month = True
            dt = dt.replace(month=int(request.POST.get('month')))
            if request.POST.get('day'):
                record.publication_has_day = True
                dt = dt.replace(day=int(request.POST.get('day')))
        record.date_of_publication = dt
    else:
        record.date_of_publication = None

    if request.FILES.get('small_cover'):
        record.small_cover = request.FILES.get('small_cover')
    if request.FILES.get('medium_cover'):
        record.medium_cover = request.FILES.get('medium_cover')
    if request.FILES.get('large_cover'):
        record.large_cover = request.FILES.get('large_cover')

    record.save()

    if request.FILES.get('ebook'):
        ebooks = request.FILES.getlist('ebook')
        for ebook in ebooks:
            ebook_file = BookFile(record=record, file=ebook)
            existing_files = record.ebooks(ebook_file.format)
            for existing_file in existing_files:
                existing_file.delete()
            ebook_file.save()

    book.subjects.clear()
    for subject in request.POST.getlist('subjects'):
        if subject.isnumeric():
            book.subjects.add(Subject.objects.get(id=subject))
        else:
            new_subject = Subject(name=subject)
            new_subject.save()
            book.subjects.add(new_subject)

    record.authors.clear()
    for author in request.POST.getlist('authors'):
        if author.isnumeric():
            record.authors.add(Author.objects.get(id=author))
        else:
            new_author = Author(name=author)
            new_author.save()
            record.authors.add(new_author)

    record.languages.clear()
    for language in request.POST.getlist('languages'):
        record.languages.add(Language.objects.get(id=language))

    publisher = request.POST.get('publisher')
    if publisher:
        if publisher.isnumeric():
            record.publisher_id = publisher
        else:
            new_publisher = Publisher(name=publisher)
            new_publisher.save()
            record.publisher = new_publisher

    record.save()

    return redirect(reverse_lazy('view_record', kwargs={'pk': record.id}))


def outgoing(request, pk=None):
    transaction = Transaction.new()
    if pk:
        transaction.record = Record.objects.get(id=pk)
    form = OutgoingForm(instance=transaction)
    return render(request, 'outgoing.html', {'form': form})


def save_outgoing(request):
    error = False
    transaction = Transaction.new()
    transaction.user_id = request.POST.get('user')
    transaction.borrow_date = request.POST.get('borrow_date')
    transaction.due_date = request.POST.get('due_date')
    transaction.record_id = request.POST.get('record')
    if request.POST.get('isbn'):
        isbn = request.POST.get('isbn')
        if isbnpy.isValid(isbn):
            if isbnpy.isI10(isbn):
                isbn = isbnpy.convert(isbn)
            try:
                transaction.record = Record.objects.get(isbn13=isbn)
            except Record.DoesNotExist:
                error = 'No books with provided ISBN in library database.'
        else:
            error = 'Invalid ISBN!'
        if error:
            raise Exception(error)
    transaction.save()
    messages.success(request, 'Book Lent!')
    return redirect(reverse_lazy('view_record', kwargs={'pk': transaction.record_id}))


def incoming(request, transaction_pk):
    transaction = Transaction.objects.get(id=transaction_pk)
    if request.POST:

        form = IncomingForm(data=request.POST, instance=transaction)
        transaction = form.save()
        if not request.POST.get('return_date'):
            transaction.return_date = datetime.today()
        transaction.save()
        messages.success(request, 'Book Returned!')
        return redirect(reverse_lazy('view_record', kwargs={'pk': transaction.record_id}))

    form = IncomingForm(instance=transaction)
    data = TransactionSerializer(transaction).data
    return render(request, 'incoming.html', {'form': form, 'data': data})


def view_record(request, pk=None):
    record = get_object_or_404(Record, pk=pk)
    transactions = Transaction.objects.filter(record=record)
    return render(request, 'view_record.html', {'record': record, 'transactions': transactions})


def list_patrons(request):
    patrons = User.objects.by_group('Patron')
    return render(request, 'list_patrons.html', {'patrons': patrons})


def view_patron(request, pk):
    patron = get_object_or_404(User, pk=pk)
    transactions = Transaction.objects.filter(user=patron)
    return render(request, 'view_patron.html', {'patron': patron, 'transactions': transactions})


def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'list_transactions.html', {'transactions': transactions})


def list_records(request):
    records = Record.objects.all()
    return render(request, 'list_records.html', {'records': records})


def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'list_authors.html', {'authors': authors})


def view_author(request, slug):
    author = Author.objects.get(slug=slug)
    return render(request, 'view_author.html', {'author': author})


def view_publisher(request, slug):
    publisher = Publisher.objects.get(slug=slug)
    return render(request, 'view_publisher.html', {'publisher': publisher})


def list_authors(request):
    objects = Author.objects.all()
    return render(request, 'list_authors.html', {'objects': objects})


def list_publishers(request):
    objects = Publisher.objects.all()
    return render(request, 'list_publishers.html', {'objects': objects})

def index(request):
    return render(request, 'library_index.html')