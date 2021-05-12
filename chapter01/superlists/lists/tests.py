from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item
import unittest

# Create your tests here.


        
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

    def test_only_saves_items_when_necessary(self):
        '''
        Test get which no data post into databaze, 
        '''
        response = self.client.get('/')
        self.assertEqual(Item.objects.count(),0)

class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        '''
        Test save post data into databaze, 
        '''
        response = self.client.post('/lists/new',data={'item_text':'A new list item'})

        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

    def test_redirects_after_POST_request(self):
        '''
        Test redirect after postsave post data into databaze, 
        '''
        response = self.client.post('/lists/new',data={'item_text':'A new list item'})

        self.assertEqual(response.status_code,302) # code 302 is redirect status code
        self.assertEqual(response['location'],'/lists/the-only-list-in-the-world/')
        # the assert abow can be replaced to the one below
        #self.assertRedirects(response, '/lists/the-only-list-in-the-world/')

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response,'list.html')

    def test_display_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        
        response = self.client.get('/lists/the-only-list-in-the-world/')
        #assertContains will check to response code too.
        self.assertContains(response,'itemey 1')
        self.assertContains(response,'itemey 2')

