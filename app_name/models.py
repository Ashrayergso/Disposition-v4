```python
from django.db import models

class PositionAndContractLength(models.Model):
    position_name = models.CharField(max_length=255)
    contract_length = models.IntegerField()
    onboard_months = models.IntegerField()
    vacation_months = models.IntegerField()

class CertificateTypesAndExpiry(models.Model):
    certificate_name = models.CharField(max_length=255)
    expiry_date = models.DateField()

class Crew(models.Model):
    name = models.CharField(max_length=255)
    position = models.ForeignKey(PositionAndContractLength, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    certificates = models.ManyToManyField(CertificateTypesAndExpiry)

class Ship(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

class ShipCrewAllowance(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    position = models.ForeignKey(PositionAndContractLength, on_delete=models.CASCADE)
    allowance_count = models.IntegerField()

class Assignment(models.Model):
    crew_member = models.ForeignKey(Crew, on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=255)

class ShipSailingSchedule(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    port_name = models.CharField(max_length=255)
    port_code = models.CharField(max_length=255)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    voyage_type = models.CharField(max_length=255)
    port_type = models.CharField(max_length=255)
```