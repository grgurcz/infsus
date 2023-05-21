from django.db import models


class Desk(models.Model):
    LOCATION_CHOICES = [
        ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'),
        ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'),
        ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'),
        ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Computer(models.Model):
    CATEGORY_CHOICES = [
        ('basic', 'Osnovno'),
        ('pro', 'Pro'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    desk = models.ForeignKey(Desk, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ComputerComponent(models.Model):
    COMPONENT_CHOICES = [
        ('processor', 'Procesor'),
        ('motherboard', 'Matična ploča'),
        ('graphics_card', 'Grafička kartica'),
    ]
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='components')
    name = models.CharField(max_length=100)
    component_type = models.CharField(max_length=40, choices=COMPONENT_CHOICES)