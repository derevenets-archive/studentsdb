# -*- coding: utf-8 -*-
# Allow us to use cyrillic text
from django.db import models


class Group(models.Model):

    """Group Model"""

    # Customisation model's behavior :
    # table's structure / view at admin
    class Meta(object):
        # Clear, readable names in admin interface
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"

    # Represents human-readable information
    # __str__ in Python 3
    def __unicode__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
        else: # there is no leader in group
            return u"%s" % self.title

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    # One to One relationship
    # Indexing one student from Students model
    leader = models.OneToOneField(
        'Student',
        verbose_name=u"Староста",
        # Can be empty
        blank=True,
        null=True,
        # Sets the null value if student deleted
        on_delete=models.SET_NULL)
