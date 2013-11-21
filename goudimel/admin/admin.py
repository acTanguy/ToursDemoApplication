from django.contrib import admin
from goudimel.models.book import Book
from goudimel.models.piece import Piece
from goudimel.models.phrase import Phrase
from goudimel.models.person import Person

def reindex_in_solr(modeladmin, request, queryset):
    for item in queryset:
        item.save()
reindex_in_solr.short_description = "Re-Index Selected Items"

class  BookAdmin(admin.ModelAdmin):
    list_display=('title', 'publisher', 'published', 'num_pages')
    list_editable = ("publisher", 'num_pages')
    list_filter = ('publisher',)
    search_fields = ('title',)
    actions = [reindex_in_solr]



class PieceAdmin(admin.ModelAdmin):
    actions = [reindex_in_solr]

class PhraseAdmin(admin.ModelAdmin):
    actions = [reindex_in_solr]

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Phrase, PhraseAdmin)
admin.site.register(Person, PersonAdmin)