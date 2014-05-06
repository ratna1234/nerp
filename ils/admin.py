from django.contrib import admin
from models import Book, Record, Author, Subject, Transaction, BookFile, LibrarySetting

admin.site.register(Book)
admin.site.register(BookFile)
admin.site.register(Record)
admin.site.register(Subject)
admin.site.register(Author)
admin.site.register(Transaction)
# admin.site.register(LibrarySetting)

class SettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(LibrarySetting, SettingsAdmin)