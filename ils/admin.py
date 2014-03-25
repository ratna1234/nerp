from django.contrib import admin
from models import Book, Record, Author, Subject, Transaction

admin.site.register(Book)
admin.site.register(Record)
admin.site.register(Subject)
admin.site.register(Author)
admin.site.register(Transaction)
