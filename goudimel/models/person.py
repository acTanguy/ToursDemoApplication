from django.db import models

class Person(models.Model):
    class Meta:
        app_label="goudimel"

    name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u"{0}".format(self.name)