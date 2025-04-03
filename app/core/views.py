from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.utils import timezone

from .models import (
    StudentPayment,
    NurseryExpense,
    ChildAttendance,
    TeacherAttendance,
    Teacher
)

from .forms import ChildRegistrationForm


def reports_dashboard(request):
    total_income = StudentPayment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = NurseryExpense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    net = total_income - total_expense

    today = timezone.now().date()

    total_children = ChildAttendance.objects.filter(date=today).count()
    present_children = ChildAttendance.objects.filter(date=today, present=True).count()
    absent_children = total_children - present_children

    total_teachers = Teacher.objects.count()
    teacher_attendance_today = TeacherAttendance.objects.filter(date=today, present=True).count()
    absent_teachers = total_teachers - teacher_attendance_today

    salaries_paid = NurseryExpense.objects.filter(category='salary').aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'net': net,
        'today_attendance': present_children,
        'absent_children': absent_children,
        'present_teachers': teacher_attendance_today,
        'absent_teachers': absent_teachers,
        'salaries_paid': salaries_paid
    }

    return render(request, 'core/reports.html', context)


def register_child(request):
    if request.method == 'POST':
        form = ChildRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/register_success.html')
    else:
        form = ChildRegistrationForm()

    return render(request, 'core/register_child.html', {'form': form})


from .forms import ChildAttendanceForm
from datetime import datetime

def record_attendance(request):
    message = ''
    if request.method == 'POST':
        form = ChildAttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.date = timezone.now().date()
            attendance.check_in_time = datetime.now().time()
            attendance.present = True
            attendance.save()
            message = 'Attendance recorded successfully!'
    else:
        form = ChildAttendanceForm()

    return render(request, 'core/record_attendance.html', {'form': form, 'message': message})


def record_checkout(request):
    message = ''
    if request.method == 'POST':
        form = ChildAttendanceForm(request.POST)
        if form.is_valid():
            child = form.cleaned_data['child']
            today = timezone.now().date()
            try:
                attendance = ChildAttendance.objects.get(child=child, date=today)
                attendance.check_out_time = datetime.now().time()
                attendance.save()
                message = 'Check-out recorded successfully!'
            except ChildAttendance.DoesNotExist:
                message = 'Child has not been checked-in yet.'
    else:
        form = ChildAttendanceForm()

    return render(request, 'core/record_checkout.html', {'form': form, 'message': message})


def home(request):
    return render(request, 'core/home.html')


from .forms import TeacherForm  # تأكد إنك عامل TeacherForm

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_teachers')  # أو home لو حابب
    else:
        form = TeacherForm()
    
    # ✅ لازم يكون فيه return في كل الحالات
    return render(request, 'core/register_teacher.html', {'form': form})

def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'core/list_teachers.html', {'teachers': teachers})


def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('list_teachers')
    else:
        form = TeacherForm(instance=teacher)

    return render(request, 'core/edit_teacher.html', {'form': form, 'teacher': teacher})


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.delete()
    return redirect('list_teachers')


from .forms import TeacherAttendanceForm, ParentForm

def record_teacher_attendance(request):
    if request.method == 'POST':
        form = TeacherAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherAttendanceForm()
    return render(request, 'core/record_teacher_attendance.html', {'form': form})

def register_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ParentForm()
    return render(request, 'core/register_parent.html', {'form': form})
