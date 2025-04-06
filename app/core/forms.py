from django import forms
from core.models import Child, Parent



class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'birth_date', 'parent']


class ChildRegistrationForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'health_notes', 'parent']



from .models import ChildAttendance

class ChildAttendanceForm(forms.ModelForm):
    class Meta:
        model = ChildAttendance
        fields = ['child']

#from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'  # أو حدد الحقول زي: ['name', 'phone', ...]

from .models import TeacherAttendance

class TeacherAttendanceForm(forms.ModelForm):
    class Meta:
        model = TeacherAttendance
        fields = ['teacher', 'date', 'check_in_time', 'check_out_time', 'present']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'check_in_time': forms.TimeInput(attrs={'type': 'time'}),
            'check_out_time': forms.TimeInput(attrs={'type': 'time'}),
            } 

from .models import Parent

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
