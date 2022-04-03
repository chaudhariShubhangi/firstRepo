from django.contrib import admin

# Register your models here.
from App1.models import Employee, Student

admin.site.register(Student)
admin.site.register(Employee)
