from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .util import STUDENT_STATUS, AC_YEAR


class City(models.Model):
    name = models.TextField(unique=True, verbose_name=_('Name'))
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'cities'
        verbose_name = _('City')
        verbose_name_plural = _('Cities')



class District(models.Model):
    city = models.ForeignKey(
        City,
        related_name='districts',
        on_delete=models.CASCADE, verbose_name=_('City'), null=True)
    name = models.TextField(unique=True, verbose_name=_('Name'))
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'districts'
        verbose_name = _('District')
        verbose_name_plural = _('Districts')


class Address(models.Model):
    street_name = models.TextField(verbose_name=_('Street name'))
    street_number = models.TextField(verbose_name=_('Street number'))
    district = models.ForeignKey(
        District,
        related_name='addresses',
        on_delete=models.CASCADE, verbose_name=_('District'))
    
    def __str__(self):
        return '{} {}, {}'.format(self.street_name, self.street_number, str(self.district))
    
    class Meta:
        db_table = 'addresses'
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')



class SchoolYear(models.Model):
    name = models.TextField(verbose_name=_('Name'))
    start_date = models.DateField(verbose_name=_('Start date'))
    end_date = models.DateField(verbose_name=_('End date'))
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'school_years'
        verbose_name = _('School Year')
        verbose_name_plural = _('School Years')


class AcademicYear(models.Model):
    name = models.CharField(max_length=50, choices=AC_YEAR, default="", verbose_name=_('Name'))
    school_year = models.ForeignKey(
        SchoolYear,
        related_name='academicyears',
        on_delete=models.CASCADE, verbose_name=_('School year'))

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'academic_years'
        verbose_name = _('Academic Year')
        verbose_name_plural = _('Academic Years')


class Employee(models.Model):
    first_name = models.TextField(verbose_name=_('First name'))
    last_name = models.TextField(verbose_name=_('Last name'))
    date_of_birth = models.DateField(verbose_name=_('Date of birth'))
    municipality_of_birth = models.ForeignKey(District, verbose_name=_('Municipality of birth'))
    phone_number = models.TextField(null=True,
                                    blank=True,
                                    verbose_name=_('Broj telefona'))
    email_address = models.EmailField(null=True,
                                      blank=True,
                                      verbose_name=_('E-mail'))
    address = models.ForeignKey(Address,
                                related_name='employees',
                                on_delete=models.CASCADE,
                                verbose_name=_('Address'))
    finished_school = models.TextField(verbose_name=_('Finished education'))
    occupation = models.TextField(verbose_name=_('Occupation'))
    note = models.TextField(verbose_name=_('Note'), null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        db_table = 'employees'
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')


class Subject(models.Model):
    name = models.TextField(verbose_name=_('Name'))
    limit = models.IntegerField(verbose_name=_('Maximum number of students'))
    professor = models.ManyToManyField(Employee, blank=True, verbose_name=_('Professor'),  related_name='professors')
    assistant = models.ManyToManyField(Employee, blank=True, verbose_name=_('Assistant'),  related_name='assistants')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subjects'
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')


class ProgrammeOfStudy(models.Model):
    name = models.TextField(verbose_name=_('Programme Name'))
    limit = models.IntegerField(verbose_name=_('Limit'))
    academic_year = models.ForeignKey(
        AcademicYear,
        related_name='programmes',
        default="",
        on_delete=models.CASCADE, verbose_name=_('Academic year'))
    subjects = models.ManyToManyField(Subject, blank=True, verbose_name=_('Subjects'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'programmes'
        verbose_name = _('Programme of Study')
        verbose_name_plural = _('Programmes of Study')


class Student(models.Model):
    first_name = models.TextField(verbose_name=_('First name'))
    last_name = models.TextField(verbose_name=_('Last name'))
    date_of_birth = models.DateField(verbose_name=_('Date of birth'))
    municipality_of_birth = models.ForeignKey(District, verbose_name=_('Municipality of birth'))
    phone_number = models.TextField(null=True,
                                    blank=True,
                                    verbose_name=_('Phone number'))
    email_address = models.EmailField(null=True,
                                      blank=True,
                                      verbose_name=_('E-mail'))
    address = models.ForeignKey(Address,
                                related_name='students',
                                on_delete=models.CASCADE,
                                verbose_name=_('Address'))
    finished_school = models.TextField(verbose_name=_('Finished school'))
    index = models.IntegerField(verbose_name=_('Index number'))
    status = models.CharField(max_length=20, choices=STUDENT_STATUS, default="", verbose_name=_('Enrolment status'))
    programme_of_study = models.ForeignKey(ProgrammeOfStudy,
                                related_name='students',
                                on_delete=models.CASCADE,
                                verbose_name=_('Programme of Study'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        db_table = 'students'
        verbose_name = _('Student')
        verbose_name_plural = _('Students')



