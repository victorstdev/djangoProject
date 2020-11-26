from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase
from django.urls import reverse, resolve
from .views import signup
# Create your tests here.

class SignUpTests(TestCase):

  def setUp(self):
    url = reverse('signup')
    self.response = self.client.get(url)

  def test_signup_status_code(self):
    self.assertEquals(response.status_code, 200)
  
  def test_signup_url_resolves_signup_view(self):
    view = resolve('/signup/')
    self.assertEquals(view.func, signup)
  
  def test_crsf(self):
    self.assertContains(self.response, 'csrfmiddlewaretoken')
  
  def test_contains_form(self):
    form = self.response.context.get('form')
    self.assertIsInstance(form, UserCreationForm)
