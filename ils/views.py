from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from ils.serializers import RecordSerializer, AuthorSerializer, PublisherSerializer, SubjectSerializer
import isbn as isbnpy
import urllib2, urllib
import json
import pprint
from models import Record, Author, Publisher, Book, Subject
import os
from django.core.files import File
from datetime import datetime

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


# Create your views here.
def acquisition(request):
    record_data = {}
    # record = None
    if request.GET.get('isbn'):
        isbn = request.GET.get('isbn')
        if isbnpy.isValid(isbn):
            # response = urllib2.urlopen('http://openlibrary.org/api/volumes/brief/json/isbn:' + isbn)
            response = urllib2.urlopen('http://localhost/1.json')
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
            book.save()
            record.pagination = data['data']['number_of_pages']
            record.format = data['details']['details']['physical_format'].lower()
            record.openlibrary_url = data['data']['url']
            record.date_of_publication = datetime.strptime(data['data']['publish_date'], '%B %d, %Y').date()
            record.openlibrary_id = data['data']['identifiers']['openlibrary'][0]
            record.goodreads_id = data['data']['identifiers']['goodreads'][0]
            record.librarything_id = data['data']['identifiers']['librarything'][0]
            record.book = book
            if new_record:
                record.date_added = datetime.today()
            record.save()
            record.book.authors.clear()
            for author in data['details']['details']['authors']:
                author_key = author['key'].replace('/authors/', '')
                try:
                    book_author = Author.objects.get(identifier=author_key)
                except Author.DoesNotExist:
                    book_author = Author(identifier=author_key)
                book_author.name = author['name']
                book_author.save()
                record.book.authors.add(book_author)

            record.book.subjects.clear()
            for subject in data['details']['details']['subjects']:
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

            # cover_url = data['data']['cover']['large']
            # result = urllib.urlretrieve(cover_url)
            # record.large_cover.save(
            #     os.path.basename(cover_url),
            #     File(open(result[0]))
            # )
            # cover_url = data['data']['cover']['medium']
            # result = urllib.urlretrieve(cover_url)
            # record.medium_cover.save(
            #     os.path.basename(cover_url),
            #     File(open(result[0]))
            # )
            # cover_url = data['data']['cover']['small']
            # result = urllib.urlretrieve(cover_url)
            # record.small_cover.save(
            #     os.path.basename(cover_url),
            #     File(open(result[0]))
            # )
            # thumbnail_url = data['details']['thumbnail_url']
            # result = urllib.urlretrieve(thumbnail_url)
            # record.small_cover.save(
            #     os.path.basename(thumbnail_url),
            #     File(open(result[0]))
            # )

            # import pdb
            #
            # pdb.set_trace()
            record_data = RecordSerializer(record).data

    return render(request, 'acquisition.html', {'data': record_data})