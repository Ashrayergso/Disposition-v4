```python
from django import forms
from .models import Crew, Ship, Assignment, ShipSailingSchedule, PositionAndContractLength, ShipCrewAllowance, CertificateTypesAndExpiry

class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = ['name', 'position', 'status', 'contract_start_date', 'contract_end_date', 'certificates']

class ShipForm(forms.ModelForm):
    class Meta:
        model = Ship
        fields = ['name', 'code', 'status', 'crew_allowance']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['crew_member', 'ship', 'start_date', 'end_date', 'status']

class ShipSailingScheduleForm(forms.ModelForm):
    class Meta:
        model = ShipSailingSchedule
        fields = ['ship', 'port_name', 'port_code', 'arrival_date', 'departure_date', 'voyage_type', 'port_type']

class PositionAndContractLengthForm(forms.ModelForm):
    class Meta:
        model = PositionAndContractLength
        fields = ['position_name', 'contract_length', 'onboard_months', 'vacation_months']

class ShipCrewAllowanceForm(forms.ModelForm):
    class Meta:
        model = ShipCrewAllowance
        fields = ['ship', 'position', 'allowance_count']

class CertificateTypesAndExpiryForm(forms.ModelForm):
    class Meta:
        model = CertificateTypesAndExpiry
        fields = ['certificate_name', 'expiry_date']
```