from django.db import models


GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female')
)

STUDENT_STATUS = (
    ('a', 'Active'),
    ('p', 'Prospective'),
    ('x', 'Inactive')
)

PAYMENT_METHOD = (
    ('CQ', 'Cheque'),
    ('CS', 'Cash')
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
        return "%s %s" % (self.first_name, self.last_name)


class Student(models.Model):
    school = models.ForeignKey(School)
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    status = models.CharField(max_length=1, choices=STUDENT_STATUS)
    house = models.ForeignKey(House)
    parent = models.ForeignKey(Parent, null=True)
    medical_information = models.TextField(null=True)
    photo_permitted = models.BooleanField(default=True)

    class Meta:
        ordering = ["-last_name"]

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Teacher(models.Model):
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    status = models.CharField(max_length=1, choices=STUDENT_STATUS)
    email_address = models.CharField(max_length=128)
    email_address2 = models.CharField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=13)
    phone_number2 = models.CharField(max_length=13, blank=True)
    physical_address = models.TextField()

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class TermDate(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=128,blank=True)
    attendances = models.ManyToManyField(Student)

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    subject_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.subject_name

class ClassGroup(models.Model):
    class_name = models.CharField(max_length=32)
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)
    students = models.ManyToManyField(Student)

    def __unicode__(self):
        return "%s Subject: %s Teacher: %s %s" % (self.class_name,
                                                  self.subject,
                                                  self.teacher.first_name,
                                                  self.teacher.last_name)
class Fee(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    student = models.ForeignKey(Student)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHOD)
    receipt_number = models.IntegerField()

    def __unicode__(self):
        return "Student: %s %s, Paid %s" % (self.student.first_name,
                                            self.student.last_name,
                                            self.paid)
