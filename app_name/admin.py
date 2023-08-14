```python
from django.contrib import admin
from .models import Crew, Ship, Assignment, ShipSailingSchedule, PositionAndContractLength, ShipCrewAllowance, CertificateTypesAndExpiry

class CrewAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'status', 'contract_start_date', 'contract_end_date')
    search_fields = ('name', 'position__position_name', 'status')

class ShipAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'status', 'crew_allowance')
    search_fields = ('name', 'code', 'status')

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('crew_member', 'ship', 'start_date', 'end_date', 'status')
    search_fields = ('crew_member__name', 'ship__name', 'status')

class ShipSailingScheduleAdmin(admin.ModelAdmin):
    list_display = ('ship', 'port_name', 'port_code', 'arrival_date', 'departure_date', 'voyage_type', 'port_type')
    search_fields = ('ship__name', 'port_name', 'port_code', 'voyage_type', 'port_type')

class PositionAndContractLengthAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'contract_length', 'onboard_months', 'vacation_months')
    search_fields = ('position_name',)

class ShipCrewAllowanceAdmin(admin.ModelAdmin):
    list_display = ('ship', 'position', 'allowance_count')
    search_fields = ('ship__name', 'position__position_name')

class CertificateTypesAndExpiryAdmin(admin.ModelAdmin):
    list_display = ('certificate_name', 'expiry_date')
    search_fields = ('certificate_name',)

admin.site.register(Crew, CrewAdmin)
admin.site.register(Ship, ShipAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(ShipSailingSchedule, ShipSailingScheduleAdmin)
admin.site.register(PositionAndContractLength, PositionAndContractLengthAdmin)
admin.site.register(ShipCrewAllowance, ShipCrewAllowanceAdmin)
admin.site.register(CertificateTypesAndExpiry, CertificateTypesAndExpiryAdmin)
```