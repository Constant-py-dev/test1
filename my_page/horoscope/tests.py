from django.test import TestCase
from django.urls import reverse
from .views import zodiac_dict

# Create your tests here.
class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_elements_group(self):
        response = self.client.get('/horoscope/elements')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Fire', response.content.decode())
        self.assertIn('Earth', response.content.decode())
        self.assertIn('Air', response.content.decode())
        self.assertIn('Water', response.content.decode())

    def test_redirect_from_num(self):
        lst = list(zodiac_dict)
        for num, sign in enumerate(lst, start=1):
            url = reverse('horoscope-number', args=(num,))
            redirected_url = reverse('horoscope-name', args=(sign,))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertURLEqual(response.url, redirected_url)

    def test_signs(self):
        for sign, description in zodiac_dict.items():
            url = reverse('horoscope-name', args=(sign,))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(description, response.content.decode())
