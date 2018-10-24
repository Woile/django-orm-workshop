from django.contrib import admin

# Register your models here.
from humanresources import models
admin.site.register(models.Regions)
admin.site.register(models.Locations)
admin.site.register(models.Jobs)
admin.site.register(models.Employees)
admin.site.register(models.Departments)
admin.site.register(models.Countries)
