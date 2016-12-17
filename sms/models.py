from __future__ import unicode_literals

from django.db import models


class School(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=13)
    address = models.TextField()

    def __unicode__(self):
        return self.name


class House(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(School)
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=128)
    house = models.ForeignKey(House)

    def __unicode__(self):
        return self.name
