from django.core.management.base import BaseCommand
from django.core.management import call_command
from master_detail.models import Computer, ComputerComponent, Desk
from random import choice

class Command(BaseCommand):
    help = 'Puni bazu s nekim podacima'

    def handle(self, *args, **options):
        call_command('flush', '--noinput')
        self.populate_desks()
        self.populate_computers()
        self.stdout.write(self.style.SUCCESS('baza napunjena'))

    def populate_desks(self):
        desk_data = [
            {'name': 'Stol 1', 'location': 'A1'},
            {'name': 'Stol 2', 'location': 'A2'},
            {'name': 'Stol 3', 'location': 'B1'},
            {'name': 'Stol 4', 'location': 'B2'},
            {'name': 'Stol 5', 'location': 'C1'},
            {'name': 'Stol 6', 'location': 'C2'},
        ]
        for desk in desk_data:
            Desk.objects.create(name=desk['name'], location=desk['location'])

    def populate_computers(self):
        desks = list(Desk.objects.all())

        computers = [
            {'name': 'Računalo 1', 'category': 'basic'},
            {'name': 'Računalo 2', 'category': 'pro'},
            {'name': 'Računalo 3', 'category': 'basic'},
            {'name': 'Računalo 4', 'category': 'pro'},
        ]
        components = [
            {'name': 'Procesor A', 'component_type': 'processor'},
            {'name': 'Procesor B', 'component_type': 'processor'},
            {'name': 'Matična ploča A', 'component_type': 'motherboard'},
            {'name': 'Matična ploča B', 'component_type': 'motherboard'},
            {'name': 'Grafička kartica A', 'component_type': 'graphics_card'},
            {'name': 'Grafička kartica B', 'component_type': 'graphics_card'},
        ]

        for computer_data in computers:
            computer = Computer.objects.create(name=computer_data['name'], category=computer_data['category'], desk=choice(desks))
            for component_data in components:
                ComputerComponent.objects.create(
                    computer=computer,
                    name=component_data['name'],
                    component_type=component_data['component_type']
                )
