import django_filters

from .models import *

################################################################################################################################################################################
############################################################################# Terminals ########################################################################################
################################################################################################################################################################################

class TerminalFilter(django_filters.FilterSet):
    terminal_name = django_filters.CharFilter(field_name='terminal_name', lookup_expr='icontains')
    iata_code     = django_filters.CharFilter(field_name='iata_code', lookup_expr='icontains')
    icao_code     = django_filters.CharFilter(field_name='icao_code', lookup_expr='icontains')

    class Meta:
        model = Terminal
        fields = ['terminal_name','iata_code', 'icao_code']

def filter_terminals(search, field):
    filtered_records = Terminal.objects.none()

    if field == "terminal_name":
        filtered_records = Terminal.objects.filter(terminal_name__icontains  = search)
    elif field == "iata_code":
        filtered_records = Terminal.objects.filter(iata_code__icontains  = search)
    elif field == "icao_code":
        filtered_records = Terminal.objects.filter(icao_code__icontains  = search)
    
    return filtered_records

################################################################################################################################################################################
############################################################################## Gates ###########################################################################################
################################################################################################################################################################################

class GateFilter(django_filters.FilterSet):
    terminal_name = django_filters.ModelChoiceFilter(field_name='terminal_name', queryset=Terminal.objects.all())
    gate_name     = django_filters.CharFilter(field_name='gate_name', lookup_expr='icontains')

    class Meta:
        model = Terminal
        fields = ['terminal_name', 'gate_name']

def filter_gates(search, field):
    filtered_records = Gate.objects.none()

    if field == "terminal_name":
        filtered_records = Gate.objects.filter(terminal_name__terminal_name__icontains  = search)
    elif field == "gate_name":
        filtered_records = Gate.objects.filter(gate_name__icontains  = search)
    
    return filtered_records

################################################################################################################################################################################
############################################################################# Stands ###########################################################################################
################################################################################################################################################################################

class StandFilter(django_filters.FilterSet):
    terminal_name = django_filters.ModelChoiceFilter(field_name='gate_name__terminal_name', queryset=Terminal.objects.all())
    gate_name  = django_filters.ModelChoiceFilter(field_name='gate_name', queryset=Gate.objects.all())
    stand_name = django_filters.CharFilter(field_name='stand_name', lookup_expr='icontains')

    class Meta:
        model = Terminal
        fields = ['terminal_name', 'gate_name', 'stand_name']

def filter_stands(search, field):
    filtered_records = Stand.objects.none()

    if field == "terminal_name":
        filtered_records = Stand.objects.filter(gate_name__terminal_name__terminal_name__icontains  = search)
    elif field == "gate_name":
        filtered_records = Stand.objects.filter(gate_name__gate_name__icontains  = search)
    elif field == "stand_name":
        filtered_records = Stand.objects.filter(stand_name__icontains  = search)
    
    return filtered_records

################################################################################################################################################################################
############################################################################# PBBs #############################################################################################
################################################################################################################################################################################

class PbbFilter(django_filters.FilterSet):
    terminal_name = django_filters.ModelChoiceFilter(field_name='stand_name__gate_name__terminal_name', queryset=Terminal.objects.all())
    gate_name  = django_filters.ModelChoiceFilter(field_name='stand_name__gate_name', queryset=Gate.objects.all())
    stand_name = django_filters.ModelChoiceFilter(field_name='stand_name', queryset=Stand.objects.all())
    pbb_name   = django_filters.CharFilter(field_name='pbb_name', lookup_expr='icontains')

    class Meta:
        model = Terminal
        fields = ['terminal_name', 'gate_name', 'stand_name', 'pbb_name']

def filter_pbbs(search, field):
    filtered_records = Pbb.objects.none()

    if field == "terminal_name":
        filtered_records = Pbb.objects.filter(stand_name__gate_name__terminal_name__terminal_name__icontains  = search)
    elif field == "gate_name":
        filtered_records = Pbb.objects.filter(stand_name__gate_name__gate_name__icontains  = search)
    elif field == "stand_name":
        filtered_records = Pbb.objects.filter(stand_name__stand_name__icontains  = search)
    elif field == "pbb_name":
        filtered_records = Pbb.objects.filter(pbb_name__icontains  = search)
    
    return filtered_records