from django.contrib import admin
from .models import (Child, Parent, Teacher, ChildAttendance,
                     TeacherAttendance,StudentPayment,NurseryExpense)

admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(ChildAttendance)
admin.site.register(TeacherAttendance)
admin.site.register(StudentPayment)
admin.site.register(NurseryExpense)
