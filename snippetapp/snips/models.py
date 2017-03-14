from django.db import models

# Create your models here.
class Snip(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    language = models.CharField(max_length=300, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    snip = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        """ returns a human readable version of the student object """
        return self.title + self.language + self.description + self.snip
