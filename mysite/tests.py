from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse

# Create your tests here.
class ThanksPage(SimpleTestCase):

    def test_contact_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_home_contact_portfolio(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
    def test_correct_templates(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mysite/contact.html')
    def test_portfolio_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_portfolio_url_name(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
    def test_correct_templates_portfolio(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mysite/portfolio.html')

