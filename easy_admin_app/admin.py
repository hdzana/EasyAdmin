from django.contrib import admin
from django.contrib.admin import widgets
from .models import *


class AppOverrides:
    formfield_overrides = {
        models.TextField: {'widget': widgets.AdminTextInputWidget},
        models.TimeField: {'widget': widgets.AdminTimeWidget(format='%H:%M')}
    }
    
@admin.register(Address)
class AddressAdmin(AppOverrides, admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(District)
class DistrictAdmin(AppOverrides, admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(City)
class CityAdmin(AppOverrides, admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
admin.site.register(SchoolYear)
admin.site.register(AcademicYear)
admin.site.register(ProgrammeOfStudy)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Employee)

