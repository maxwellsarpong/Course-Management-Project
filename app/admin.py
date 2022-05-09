from django.contrib import admin
from .models import Delegate, Registration, Course, CourseFee, CourseType, Location, Booking, Invoice, Employee

# Register your models here.
admin.site.site_header = 'Course Management'
admin.site.site_title = 'Course Management'
admin.site.index_title = 'Course Management'
admin.site.register(Delegate)
admin.site.register(Registration)
admin.site.register(Course)
admin.site.register(CourseFee)
admin.site.register(CourseType)
admin.site.register(Location)
admin.site.register(Booking)
admin.site.register(Invoice)
admin.site.register(Employee)
