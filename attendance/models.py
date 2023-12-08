from django.db import models
from accounts.models import CustomUser

class Shift(models.Model):
    BLUE         = "primary"
    LIGHT_BLUE   = "info"
    GRAY         = "secondary"
    LIGHT_GRAY   = "light"
    GREEN        = "success"
    LIGHT_GREEN  = "success-l"
    RED          = "danger"
    LIGHT_RED    = "danger-l"
    YELLOW       = "warning"
    LIGHT_YELLOW = "warning-l"
    BLACK        = "dark"

    COLOR_CHOICES  = [
        (BLUE, "Blue"),
        (LIGHT_BLUE, "Light Blue"),
        (GRAY, "Gray"),
        (LIGHT_GRAY, "Light Gray"),
        (GREEN, "Green"),
        (LIGHT_GREEN, "Light Green"),
        (RED, "Red"),
        (LIGHT_RED, "Light Red"),
        (YELLOW, "Yellow"),
        (LIGHT_YELLOW, "Light Yellow"),
        (BLACK, "Black"),
    ]

    name      = models.CharField(max_length=20, blank=False, null=False)
    from_time = models.TimeField(blank=True, null=True)
    to_time   = models.TimeField(blank=True, null=True)
    color     = models.CharField(max_length=100, blank=True, null=True, choices=COLOR_CHOICES, default=LIGHT_GRAY)
    def __str__(self):
        return f'{self.name}'

class AttendanceRecord(models.Model):
    PRESENT         = "PR"
    ABSENT          = "AB"
    SICK_LEAVE      = "SL"
    EMERGENCY_LEAVE = "EM"

    STATUS_CHOICES  = [
        (PRESENT, "Present"),
        (ABSENT, "Absent"),
        (SICK_LEAVE, "Sick Leave"),
        (EMERGENCY_LEAVE, "Emergency Leave"),
    ]
    
    employee = models.ForeignKey(CustomUser, blank=False, null=False, on_delete=models.CASCADE)
    shift    = models.ForeignKey(Shift, blank=False, null=False, on_delete=models.CASCADE)
    date     = models.DateField(blank=True, null=True)
    status   = models.CharField(max_length=100, blank=True, null=True, choices=STATUS_CHOICES, default=PRESENT)
    class Meta:
        # Enforce uniqueness for the combination of field1 and field2
        unique_together = ('employee', 'shift','date')
    def __str__(self):
        return f'{self.employee} - {self.date} - {self.status}'