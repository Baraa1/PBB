from django.db import models

class Terminal(models.Model):
    terminal_name = models.CharField(max_length=50, blank=False, null=False)
    iata_code = models.CharField(max_length=10, blank=False, null=False, default='unset')
    icao_code = models.CharField(max_length=10, blank=False, null=False, default='unset')

    def __str__(self):
        return f'{self.iata_code}'

class Gate(models.Model):
    terminal_name = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    gate_name     = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f'Gate {self.gate_name} | {self.terminal_name} |'

class Stand(models.Model):
    gate_name  = models.ForeignKey(Gate, on_delete=models.CASCADE)
    stand_name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f'{self.stand_name}'

class Pbb(models.Model):
    stand_name = models.ForeignKey(Stand, on_delete=models.CASCADE)
    pbb_name   = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f'PBB {self.pbb_name} | {self.stand_name.gate_name.terminal_name} |'