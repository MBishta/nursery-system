from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    health_notes = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    specialization = models.CharField(max_length=100)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ChildAttendance(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.child.first_name} - {self.date}"

class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.teacher.first_name} - {self.date}"

class StudentPayment(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=[
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank', 'Bank Transfer')
    ])
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.child.first_name} - {self.amount} - {self.payment_date}"

class NurseryExpense(models.Model):
    expense_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=100, choices=[
        ('salary', 'Salary'),
        ('supplies', 'Supplies'),
        ('rent', 'Rent'),
        ('utilities', 'Utilities'),
        ('maintenance', 'Maintenance'),
        ('other', 'Other')
    ])
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.amount} - {self.expense_date}"
