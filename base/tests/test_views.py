from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class LoginPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')
        self.user_data = {'username': 'testuser', 'password': 'testpassword'}
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_authenticated_user_redirected_to_home(self):
        self.client.force_login(self.user)
        response = self.client.get(self.login_url)
        self.assertRedirects(response, self.home_url)

    def test_valid_login_redirects_to_home(self):
        response = self.client.post(self.login_url, data=self.user_data)
        self.assertRedirects(response, self.home_url)

    def test_invalid_login_shows_error_message(self):
        response = self.client.post(self.login_url, data={'username': 'nonexistent', 'password': 'invalid'})
        self.assertContains(response, 'Username or Password does not exist')

    def test_logout_user_redirected_to_home(self):
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.home_url)
