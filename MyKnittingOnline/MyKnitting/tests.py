from django.test import TestCase
from MyKnitting.models import Project
from MyKnitting.views import *
from django.urls import reverse


# Create your tests here.
class LoggedInTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        Project.objects.create(owner=self.user, title='NewProject', completed=False, public=False)

    def test_index_view(self):
        response = self.client.get(reverse('MyKnitting:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Maybe in the future there will be smth like knitting social media, but now I'm not promising that.")

    def test_project_view(self):
        response = self.client.get(reverse('MyKnitting:projects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your projects:")
        self.assertContains(response, 'NewProject')

class NotLoggedInTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('MyKnitting:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User not logged")
    def test_project_view(self):
        response = self.client.get(reverse('MyKnitting:projects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User not logged")