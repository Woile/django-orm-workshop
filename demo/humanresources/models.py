# Known Third Party Files
from django.db import models
from django.core.validators import MinValueValidator


class Regions(models.Model):
    region_name = models.CharField(max_length=25)


class Countries(models.Model):
    country_iso_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=40)
    region = models.ForeignKey(Regions, blank=True, null=True, on_delete=models.SET_NULL)


class Locations(models.Model):
    street_address = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=12)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=25)
    country = models.ForeignKey(Countries, blank=True, null=True, on_delete=models.SET_NULL)


class Departments(models.Model):
    department_name = models.CharField(max_length=30)
    manager = models.ForeignKey("Employees", blank=True, null=True, on_delete=models.SET_NULL, db_constraint=False)
    location = models.ForeignKey(Locations, blank=True, null=True, on_delete=models.SET_NULL)


class Jobs(models.Model):
    job_code = models.CharField(max_length=10, unique=True, default='JOB')
    job_title = models.CharField(max_length=35)
    min_salary = models.FloatField()
    max_salary = models.FloatField()


class Employees(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    hire_date = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Jobs, blank=True, null=True, on_delete=models.SET_NULL)
    salary = models.FloatField(validators=[MinValueValidator(0)])
    manager = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Departments, blank=True, null=True, on_delete=models.SET_NULL)
    commission_pct = models.FloatField(null=True)
    phone_number = models.CharField(max_length=30, null=True)
