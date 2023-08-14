```python
from django.test import TestCase
from .models import Crew, Ship, Assignment, ShipSailingSchedule, PositionAndContractLength, ShipCrewAllowance, CertificateTypesAndExpiry

class CrewModelTest(TestCase):
    def setUp(self):
        self.crew = Crew.objects.create(name='John Doe', position='Captain', status='Active')

    def test_crew_creation(self):
        self.assertEqual(self.crew.name, 'John Doe')

class ShipModelTest(TestCase):
    def setUp(self):
        self.ship = Ship.objects.create(name='Titanic', code='TNC', status='Active')

    def test_ship_creation(self):
        self.assertEqual(self.ship.name, 'Titanic')

class AssignmentModelTest(TestCase):
    def setUp(self):
        self.crew = Crew.objects.create(name='John Doe', position='Captain', status='Active')
        self.ship = Ship.objects.create(name='Titanic', code='TNC', status='Active')
        self.assignment = Assignment.objects.create(crew_member=self.crew, ship=self.ship, status='Assigned')

    def test_assignment_creation(self):
        self.assertEqual(self.assignment.crew_member.name, 'John Doe')
        self.assertEqual(self.assignment.ship.name, 'Titanic')

class ShipSailingScheduleModelTest(TestCase):
    def setUp(self):
        self.ship = Ship.objects.create(name='Titanic', code='TNC', status='Active')
        self.schedule = ShipSailingSchedule.objects.create(ship=self.ship, port_name='New York', port_code='NYC')

    def test_schedule_creation(self):
        self.assertEqual(self.schedule.ship.name, 'Titanic')
        self.assertEqual(self.schedule.port_name, 'New York')

class PositionAndContractLengthModelTest(TestCase):
    def setUp(self):
        self.position = PositionAndContractLength.objects.create(position_name='Captain', contract_length=12)

    def test_position_creation(self):
        self.assertEqual(self.position.position_name, 'Captain')

class ShipCrewAllowanceModelTest(TestCase):
    def setUp(self):
        self.ship = Ship.objects.create(name='Titanic', code='TNC', status='Active')
        self.position = PositionAndContractLength.objects.create(position_name='Captain', contract_length=12)
        self.allowance = ShipCrewAllowance.objects.create(ship=self.ship, position=self.position, allowance_count=1)

    def test_allowance_creation(self):
        self.assertEqual(self.allowance.ship.name, 'Titanic')
        self.assertEqual(self.allowance.position.position_name, 'Captain')

class CertificateTypesAndExpiryModelTest(TestCase):
    def setUp(self):
        self.certificate = CertificateTypesAndExpiry.objects.create(certificate_name='First Aid', expiry_date='2022-12-31')

    def test_certificate_creation(self):
        self.assertEqual(self.certificate.certificate_name, 'First Aid')
```