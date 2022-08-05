from django.test import SimpleTestCase
from django.urls import resolve,reverse
import template.views import * 

class TestUrls(SimpleTestCase):
     def test_list_url_resolved(self):
         assert 1==2
         url = reverse('login')
         self.assertEquals(resolve(url).func,loginPage)

