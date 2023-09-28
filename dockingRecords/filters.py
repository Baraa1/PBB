import django_filters

from accounts.models import CustomUser
from locations.models import Terminal, Gate, Stand
from .models import *

class RecordFilter(django_filters.FilterSet):
    terminal   = django_filters.ModelChoiceFilter(field_name='stand__gate_name__terminal_name', queryset=Terminal.objects.all())
    stand      = django_filters.ModelChoiceFilter(field_name='stand', queryset=Stand.objects.all())
    operator1  = django_filters.ModelChoiceFilter(field_name='operator1', queryset=CustomUser.objects.all())
    operator2  = django_filters.ModelChoiceFilter(field_name='operator2', queryset=SecondOperator.objects.all())
    flight_no1 = django_filters.CharFilter(field_name='flight_no1', lookup_expr='icontains')
    ac_type    = django_filters.CharFilter(field_name='ac_type', lookup_expr='icontains')
    ac_reg     = django_filters.CharFilter(field_name='ac_reg', lookup_expr='icontains')
    flight_no2 = django_filters.CharFilter(field_name='flight_no2', lookup_expr='icontains')
    docked     = django_filters.DateTimeFilter(field_name='docked', lookup_expr='gte')
    docked_d   = django_filters.DateTimeFilter(field_name='docked', lookup_expr='lte')
    undocked   = django_filters.DateTimeFilter(field_name='undocked', lookup_expr='gte')
    undocked_d = django_filters.DateTimeFilter(field_name='undocked', lookup_expr='lte')
    chocks_on  = django_filters.TimeFilter(field_name='chocks_on', lookup_expr='gte')
    door_close = django_filters.TimeFilter(field_name='door_close', lookup_expr='gte')

    class Meta:
        model = DockingRecord
        fields = ['terminal', 'stand', 'operator1', 'flight_no1', 'ac_type', 'ac_reg', 'flight_no2', 'docked', 'undocked', 'chocks_on', 'door_close', 'no_docking']

def filter_records(search, field):
    filtered_records = DockingRecord.objects.none()

    if field == "operator1":
        filtered_records = DockingRecord.objects.filter(operator1__username__icontains  = search).order_by('-time_stamp')[:50]

    elif field == "ac_type":
        filtered_records = DockingRecord.objects.filter(ac_type__icontains    = search).order_by('-time_stamp')[:50]

    elif field == "ac_reg":
        filtered_records = DockingRecord.objects.filter(ac_reg__icontains     = search).order_by('-time_stamp')[:50]

    elif field == "flight_no1":
        filtered_records = DockingRecord.objects.filter(flight_no1__icontains = search).order_by('-time_stamp')[:50]

    elif field == "flight_no2":
        filtered_records = DockingRecord.objects.filter(flight_no2__icontains = search).order_by('-time_stamp')[:50]
    
    return filtered_records