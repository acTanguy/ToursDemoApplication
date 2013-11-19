from django.db import models


class Piece(models.Model):
    class Meta:
        app_label = "goudimel"

    book_id = models.ForeignKey("goudimel.Book", related_name="pieces")
    title = models.CharField(max_length=64, blank=True, null=True)
    composer_src = models.ForeignKey("goudimel.Person", blank=True, null=True)
    forces = models.CharField(max_length=16, blank=True, null=True)
    print_concordances = models.CharField(max_length=128, blank=True, null=True)
    ms_concordances = models.CharField(max_length=128, blank=True, null=True)
    pdf_link = models.URLField(max_length=255, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{0}".format(self.title)