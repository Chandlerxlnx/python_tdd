from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
import unittest

# Create your tests here.


class SmakeTest(TestCase):
    @unittest.skip
    #@django.test.skip
    def test_bad_maths(self):
        self.assertEqual(1+1,3)
        
class HommePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)