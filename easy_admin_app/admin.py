from django.contrib import admin
from django.contrib.admin import widgets
from .models import *


class AppOverrides:
    formfield_overrides = {
        models.TextField: {'widget': widgets.AdminTextInputWidget},
        models.TimeField: {'widget': widgets.AdminTimeWidget(format='%H:%M')}
    }
admin.site.register(City)
admin.site.register(District)
admin.site.register(Address)