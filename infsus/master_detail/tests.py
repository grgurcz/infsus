from django.test import TestCase, Client
from django.urls import reverse

from .models import Computer, Desk, ComputerComponent

class ComputerAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.desk1 = Desk.objects.create(name='Stol 1', location='A1')
        self.desk2 = Desk.objects.create(name='Stol 2', location='A2')
        self.computer1 = Computer.objects.create(name='Racunalo 1', category='basic', desk=self.desk1)
        self.computer2 = Computer.objects.create(name='Racunalo 2', category='pro', desk=self.desk2)
        self.component1 = ComputerComponent.objects.create(computer=self.computer1, name='Procesor A', component_type='processor')
        self.component2 = ComputerComponent.objects.create(computer=self.computer2, name='Graficka kartica A', component_type='graphics_card')

    def test_computer_list_view(self):
        url = reverse('computer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master_detail/computer_list.html')
        self.assertContains(response, self.computer1.name)
        self.assertContains(response, self.computer2.name)

    def test_computer_add_view(self):
        url = reverse('computer_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master_detail/computer_form.html')

        data = {'name': 'Novo racunalo', 'category': 'basic'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_computer_edit_view(self):
        url = reverse('computer_edit', kwargs={'pk': self.computer1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master_detail/computer_edit.html')

        data = {'name': 'Promijenjeno racunalo', 'category': 'basic'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)


    def test_computer_delete_view(self):
        url = reverse('computer_delete', kwargs={'pk': self.computer1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_desk_list_view(self):
        url = reverse('desk_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master_detail/desk_list.html')
        self.assertContains(response, self.desk1.name)
        self.assertContains(response, self.desk2.name)

    def test_desk_add_view(self):
        url = reverse('desk_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master_detail/desk_form.html')

        data = {'name': 'Novi stol', 'location': 'A3'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_desk_edit_view(self):
        url = reverse('desk_edit', kwargs={'pk': self.desk1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master_detail/desk_form.html')

        data = {'name': 'Promijenjeni stol', 'location': 'A1'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_desk_delete_view(self):
        url = reverse('desk_delete', kwargs={'pk': self.desk1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_component_create_view(self):
        url = reverse('component_create', kwargs={'pk': self.computer1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master_detail/component_create.html')

        data = {'name': 'Novi procesor', 'component_type': 'processor'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_component_edit_view(self):
        url = reverse('component_edit', kwargs={'pk': self.component1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master_detail/component_edit.html')

        data = {'name': 'Promijenjeni procesor', 'component_type': 'processor'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_component_delete_view(self):
        url = reverse('component_delete', kwargs={'pk': self.component1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
