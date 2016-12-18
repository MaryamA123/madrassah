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

class Parent(models.Model):
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    email_address = models.CharField(max_length=128)
    email_address2 = models.CharField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=13)
    phone_number2 = models.CharField(max_length=13, blank=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Student(models.Model):
    school = models.ForeignKey(School)
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=128)
    house = models.ForeignKey(House)
    parent = models.ForeignKey(Parent, null=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
