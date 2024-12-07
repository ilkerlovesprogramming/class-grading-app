from django.contrib import admin
from .models import Student, Course, CompletedCourse, OngoingCourse

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CompletedCourse)
admin.site.register(OngoingCourse)