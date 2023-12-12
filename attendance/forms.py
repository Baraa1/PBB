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
            'total_hours',
            'allowance',
            'color',
            ]
        widgets = {
            "from_time": forms.TimeInput(attrs={"type":"time"}),
            "to_time": forms.TimeInput(attrs={"type":"time"}),
            "total_hours": forms.NumberInput(attrs={"type":"number"}),
            "allowance": forms.NumberInput(attrs={"type":"number"}),
        }