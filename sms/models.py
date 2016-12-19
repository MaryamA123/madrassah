from __future__ import unicode_literals

from django.db import models


GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female')
)

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
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email_address = models.CharField(max_length=128)
    email_address2 = models.CharField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=13)
    phone_number2 = models.CharField(max_length=13, blank=True)
    physical_address = models.TextField(null=True)
    post_code = models.CharField(max_length=10, null=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Student(models.Model):
    school = models.ForeignKey(School)
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    house = models.ForeignKey(House)
    parent = models.ForeignKey(Parent, null=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Teacher(models.Model):
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email_address = models.CharField(max_length=128)
    email_address2 = models.CharField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=13)
    phone_number2 = models.CharField(max_length=13, blank=True)
    physical_address = models.TextField()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Term(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=128,blank=True)
    attendances = models.ManyToManyField(Student)

    def __unicode__(self):
        return self.name
