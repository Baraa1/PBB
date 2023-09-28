# Python
from datetime import datetime
# Django
from django import forms
# Custom
from locations.models import Stand
from .models import DockingRecord

# to prepopulate datetime and time fields
date = datetime.now()
today = str(datetime.date(date))
now = str(datetime.timetz(date))
today_now = f'{today}T{now[:5]}'

class CreateDockingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only stands of the current user location
        are given as options"""

        self.request = kwargs.pop('request')
        super(CreateDockingForm, self).__init__(*args, **kwargs)
        # removes the stands of other locations from the choices
        self.fields['stand'].queryset = Stand.objects.filter(gate_name__terminal_name = self.request.user.location)

    class Meta:
        model = DockingRecord
        fields = [
            'operator1',
            'stand',
            'flight_no1',
            'ac_type',
            'ac_reg',
            'docked',
            'chocks_on',
            'b_used',
            'c_used',
            'b_docked',
            'c_docked',
            'remarks',
            ]
        widgets = {
            "operator1": forms.TextInput(attrs={"type":"text"}),
            "flight_no1": forms.TextInput(attrs={"list":"flight_no1"}),
            "ac_type": forms.TextInput(attrs={"list":"ac_type"}),
            "ac_reg": forms.TextInput(attrs={"list":"ac_reg"}),
            "docked":    forms.DateTimeInput(attrs={"type":"datetime-local", "value":today_now}),
            "chocks_on": forms.TimeInput(attrs={"type":"time", "value":now[:5]}),
            "b_docked":  forms.TimeInput(attrs={"type":"time"}),
            "c_docked":  forms.TimeInput(attrs={"type":"time"}),
        }
        help_texts = {
            'stand':      'Required',
            'flight_no1': 'Required',
            'ac_type':    'Required',
            'ac_reg':     'Required',
            'docked':     'Required',
            'chocks_on':  'Required',
        }

    def clean(self):
        # Makes these required without conditions
        required_fields = ['flight_no1', 'chocks_on', 'docked']
        for field in required_fields:
            if self.cleaned_data[field] == None:
                msg = forms.ValidationError("This field is required.")
                self.add_error(field, msg)

        b_used = self.cleaned_data.get('b_used')
        c_used = self.cleaned_data.get('c_used')

        # if user checked b_used then they must fill b_docked field
        if b_used and self.cleaned_data['b_docked'] == None:
            msg = forms.ValidationError("This field is required.")
            self.add_error('b_docked', msg)
        elif not b_used and self.cleaned_data['b_docked'] != None:
            # Keep the database consistent. The user may have
            # submitted bravo docking time even if b_used
            # was not selected
            self.cleaned_data['b_docked'] = None
        if c_used and self.cleaned_data['c_docked'] == None:
            msg = forms.ValidationError("This field is required.")
            self.add_error('c_docked', msg)
        elif not c_used and self.cleaned_data['c_docked'] != None:
            self.cleaned_data['c_docked'] = None

        return self.cleaned_data
    
class CreateUndockingForm(forms.ModelForm):
    class Meta:
        model = DockingRecord
        fields = [
            'operator2',
            'flight_no2',
            'door_close',
            'b_door_close',
            'c_door_close',
            'undocked',
            'b_used',
            'c_used',
            'b_undocked',
            'c_undocked',
            'remarks',
            ]
        widgets = {
            "operator2":  forms.TextInput(attrs={"type":"text"}),
            "undocked":   forms.DateTimeInput(attrs={"type":"datetime-local"}),
            "door_close": forms.TimeInput(attrs={"type":"time"}),
            "b_door_close": forms.TimeInput(attrs={"type":"time"}),
            "c_door_close": forms.TimeInput(attrs={"type":"time"}),
            "b_undocked": forms.TimeInput(attrs={"type":"time"}),
            "c_undocked": forms.TimeInput(attrs={"type":"time"}),
        }
        help_texts = {
            'operator2': 'Required',
            'flight_no2': 'Required',
            'door_close': 'Required',
            'b_door_close': 'Required',
            'c_door_close': 'Required',
            'undocked': 'Required',
        }

#    def fields_required(self, required_fields):
#        """Used for conditionally marking fields as required."""
#        for field in required_fields:
#            print(self.cleaned_data[field])
#            print(self.cleaned_data[field] == None)
#            if self.cleaned_data[field] == None:
#                msg = forms.ValidationError("This field is required.")
#                self.add_error(field, msg)

    def clean(self):
        # Makes these required without conditions
        required_fields = ['flight_no2', 'door_close', 'undocked']
        for field in required_fields:
            if self.cleaned_data[field] == None:
                msg = forms.ValidationError("This field is required.")
                self.add_error(field, msg)
        
        ## conditionally makes these fields required        
        b_used = self.cleaned_data.get('b_used')
        c_used = self.cleaned_data.get('c_used')

        # if user checked b_used then they must fill b_docked field
        if b_used and (self.cleaned_data['b_undocked'] == None or self.cleaned_data['b_door_close'] == None):
            msg = forms.ValidationError("This field is required.")
            self.add_error('b_undocked', msg)
        elif not b_used and self.cleaned_data['b_undocked'] != None:
            # Keep the database consistent. The user may have
            # submitted bravo docking time even if b_used
            # was not selected
            self.cleaned_data['b_undocked'] = None
        if c_used and (self.cleaned_data['c_undocked'] == None or self.cleaned_data['c_door_close'] == None):
            msg = forms.ValidationError("This field is required.")
            self.add_error('c_undocked', msg)
        elif not c_used and self.cleaned_data['c_undocked'] != None:
            self.cleaned_data['c_undocked'] = None

        return self.cleaned_data

class CreateNoDockingForm(forms.ModelForm):
    class Meta:
        model = DockingRecord
        fields = [
            'no_docking',
            'stand',
            'operator2',
            'flight_no2',
            'ac_type',
            'ac_reg',
            'door_close',
            'b_door_close',
            'c_door_close',
            'undocked',
            'b_used',
            'c_used',
            'b_undocked',
            'c_undocked',
            'remarks',
            ]
        widgets = {
            "operator2": forms.TextInput(attrs={"type":"text"}),
            "ac_type": forms.TextInput(attrs={"list":"ac_type"}),
            "ac_reg": forms.TextInput(attrs={"list":"ac_reg"}),
            "undocked":    forms.DateTimeInput(attrs={"type":"datetime-local", "value":today_now}),
            "door_close": forms.TimeInput(attrs={"type":"time", "value":now[:5]}),
            "b_door_close": forms.TimeInput(attrs={"type":"time"}),
            "c_door_close": forms.TimeInput(attrs={"type":"time"}),
            "b_undocked":  forms.TimeInput(attrs={"type":"time"}),
            "c_undocked":  forms.TimeInput(attrs={"type":"time"}),
        }
        help_texts = {
            'stand': 'Required',
            'operator2': 'Required',
            'flight_no2': 'Required',
            'ac_type': 'Required',
            'ac_reg': 'Required',
            'undocked': 'Required',
            'door_close': 'Required',
        }

    def clean(self):
        # Makes these required without conditions
        required_fields = ['flight_no2', 'door_close', 'undocked']
        for field in required_fields:
            if self.cleaned_data[field] == None:
                msg = forms.ValidationError("This field is required.")
                self.add_error(field, msg)

        b_used = self.cleaned_data.get('b_used')
        c_used = self.cleaned_data.get('c_used')

        # if user checked b_used then they must fill b_docked field
        if b_used and self.cleaned_data['b_undocked'] == None:
            msg = forms.ValidationError("This field is required.")
            self.add_error('b_undocked', msg)
        elif not b_used and self.cleaned_data['b_undocked'] != None:
            # Keep the database consistent. The user may have
            # submitted bravo docking time even if b_used
            # was not selected
            self.cleaned_data['b_undocked'] = None
        if c_used and self.cleaned_data['c_undocked'] == None:
            msg = forms.ValidationError("This field is required.")
            self.add_error('c_undocked', msg)
        elif not c_used and self.cleaned_data['c_undocked'] != None:
            self.cleaned_data['c_undocked'] = None

        return self.cleaned_data

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = DockingRecord
        fields = [
            'stand',
            'operator1',
            'operator2',
            'ac_type',
            'ac_reg',
            'flight_no1',
            'flight_no2',
            'chocks_on',
            'docked',
            'door_close',
            'b_door_close',
            'c_door_close',
            'undocked',
            'b_used',
            'c_used',
            'b_docked',
            'b_undocked',
            'c_docked',
            'c_undocked',
            'remarks',
            ]
        widgets = {
            "chocks_on":  forms.TimeInput(attrs={"type":"time"}),
            "docked":     forms.DateTimeInput(attrs={"type":"datetime-local"}),
            "door_close": forms.TimeInput(attrs={"type":"time"}),
            "b_door_close": forms.TimeInput(attrs={"type":"time"}),
            "c_door_close": forms.TimeInput(attrs={"type":"time"}),
            "undocked":   forms.DateTimeInput(attrs={"type":"datetime-local"}),
            "b_docked":   forms.TimeInput(attrs={"type":"time"}),
            "b_undocked": forms.TimeInput(attrs={"type":"time"}),
            "c_docked":   forms.TimeInput(attrs={"type":"time"}),
            "c_undocked": forms.TimeInput(attrs={"type":"time"}),
        }