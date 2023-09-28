from django.db import models
from locations.models import Stand
from accounts.models import CustomUser

# Solves the issue of having two foreign keys with the same model
class SecondOperator(models.Model):
    second_operator  = models.OneToOneField(CustomUser, blank=False, null=True, unique=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.second_operator}'


class DockingRecord(models.Model):
    # Always required
    stand      = models.ForeignKey(Stand, blank=False, null=True, on_delete=models.SET_NULL)
    ac_type    = models.CharField(max_length=10, blank=False, null=False)
    ac_reg     = models.CharField(max_length=10, blank=False, null=False)
    # Required at docking
    operator1  = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)
    flight_no1 = models.CharField(max_length=10, blank=True, null=True)
    docked     = models.DateTimeField(blank=True, null=True)
    chocks_on  = models.TimeField(blank=True, null=True)
    # Required at undocking or no docking
    operator2    = models.ForeignKey(SecondOperator, blank=True, null=True, on_delete=models.SET_NULL)
    flight_no2   = models.CharField(max_length=10, blank=True, null=True)
    door_close   = models.TimeField(blank=True, null=True)
    b_door_close = models.TimeField(blank=True, null=True)
    c_door_close = models.TimeField(blank=True, null=True)
    undocked     = models.DateTimeField(blank=True, null=True)

    # not required but it tells the view how to read this record
    # false means this is a full record
    # true means this is an undocking record only, no docking was recorded for this flight
    no_docking = models.BooleanField(blank=True, null=True, default=False)
    # true means pbb b was used so make b_docked required
    b_used   = models.BooleanField(blank=True, null=True, default=False)
    # true means pbb c was used so make c_docked required
    c_used   = models.BooleanField(blank=True, null=True, default=False)

    # Required if b_used is true
    b_docked   = models.TimeField(blank=True, null=True)
    # Required if c_used is true
    c_docked   = models.TimeField(blank=True, null=True)
    # Required if b_used is true and undocking
    b_undocked = models.TimeField(blank=True, null=True)
    # Required if c_used is true and undocking
    c_undocked = models.TimeField(blank=True, null=True)
    
    remarks    = models.TextField(blank=True,  null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.stand} - {self.operator1} - {self.ac_type} - {self.time_stamp}'
