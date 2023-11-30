from django import forms
from .models import AttendanceRecord, Shift

class CreateAttendanceRecordForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = [
            'employee',
            'shift',
            'date',
            ]
        widgets = {
            "employee": forms.TextInput(),
            "shift":    forms.TextInput(),
            "date":     forms.TextInput(),
        }

class CreateShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = [
            'name',
            'from_time',
            'to_time',
            'color',
            ]
        widgets = {
            "from_time": forms.TimeInput(attrs={"type":"time"}),
            "to_time": forms.TimeInput(attrs={"type":"time"}),
        }