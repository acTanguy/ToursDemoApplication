from django.contrib import admin
from goudimel.models.book import Book
from goudimel.models.piece import Piece
from goudimel.models.phrase import Phrase
from goudimel.models.person import Person

class  BookAdmin(admin.ModelAdmin):
    list_display=('title', 'publisher', 'published', 'num_pages')
    list_editable = ("publisher", 'num_pages')
    list_filter = ('publisher',)
    search_fields = ('title',)
class PieceAdmin(admin.ModelAdmin):
    pass

class PhraseAdmin(admin.ModelAdmin):
    pass

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Phrase, PhraseAdmin)
admin.site.register(Person, PersonAdmin)