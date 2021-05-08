from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item
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

    #@unittest.skip
    def test_home_page_returns_correct_html(self):
        request = HttpRequest() # create HttpRequest object, 用户在浏览器中请求网页时，Django看到的就是HttpRequest对象
        response = home_page(request) # 把request传给homepage视图
        
        html = response.content.decode('utf8') # 提取content,转为html字符串
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))

    def test_uses_home_temp(self):
        #assertTemplateUsed need work with client
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/',data={'item_text':'A new list item'})
        self.assertIn('A new list item',response.content.decode())
        
class ItemModelTest(TestCase):
    '''ORM test'''
    def test_saving_and_retrieving_item(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item=saved_items[0]
        second_saved_item=saved_items[1]
        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(second_saved_item.text,'item the second')

