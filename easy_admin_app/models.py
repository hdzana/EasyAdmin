from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


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
