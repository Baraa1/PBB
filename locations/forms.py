from django import forms
from .models import *

class CreateTerminalForm(forms.ModelForm):
    class Meta:
        model = Terminal
        fields = [
            'terminal_name',
            'iata_code',
            'icao_code',
            ]

class UpdateTerminalForm(forms.ModelForm):
    class Meta:
        model = Terminal
        fields = [
            'terminal_name',
            'iata_code',
            'icao_code',
            ]

class CreateGateForm(forms.ModelForm):
    class Meta:
        model = Gate
        fields = [
            'terminal_name',
            'gate_name',
            ]

class UpdateGateForm(forms.ModelForm):
    class Meta:
        model = Gate
        fields = [
            'terminal_name',
            'gate_name',
            ]

class CreateStandForm(forms.ModelForm):
    class Meta:
        model = Stand
        fields = [
            'gate_name',
            'stand_name',
            ]

class UpdateStandForm(forms.ModelForm):
    class Meta:
        model = Stand
        fields = [
            'gate_name',
            'stand_name',
            ]

class CreatePbbForm(forms.ModelForm):
    class Meta:
        model = Pbb
        fields = [
            'stand_name',
            'pbb_name',
            ]

class UpdatePbbForm(forms.ModelForm):
    class Meta:
        model = Pbb
        fields = [
            'stand_name',
            'pbb_name',
            ]