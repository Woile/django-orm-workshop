# Known Third Party Files
from django.db import models
from django.core.validators import MinValueValidator


class Regions(models.Model):
    region_name = models.CharField(max_length=25)

    def __str__(self):
        return f'region: {self.region_name}'


class Countries(models.Model):
    country_iso_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=40)
    region = models.ForeignKey(Regions, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'iso: {self.country_iso_code} name: {self.country_name}'


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

    def __str__(self):
        return f'{self.department_name}'


class Jobs(models.Model):
    job_code = models.CharField(max_length=10, unique=True, default='JOB')
    job_title = models.CharField(max_length=35)
    min_salary = models.FloatField()
    max_salary = models.FloatField()

    def __str__(self):
        return f'job_code: {self.job_code} job_title: {self.job_title} min_salary: {self.min_salary} max_salary: {self.max_salary}'


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

    def __self__(self):
        return f'first_name: {self.first_name} last_name: {self.last_name}'