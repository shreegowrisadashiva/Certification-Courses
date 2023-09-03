from django.contrib import admin
from hello.models  import Student, Payment, Project, department, Course, Faculty

# Register your models here.
admin.site.register(Student)
admin.site.register(Payment)
admin.site.register(Project)
admin.site.register(department)
admin.site.register(Course)
admin.site.register(Faculty)
