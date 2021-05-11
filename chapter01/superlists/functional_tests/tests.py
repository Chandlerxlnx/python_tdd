# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:23:34 2021

@author: Chandler
"""

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

MAX_WAIT =10
class NewVistorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
        
        
    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row.text for row in rows])
                return
            except (AssertionError,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        
        self.browser.get(self.live_server_url)
        
        #网页应该包含“to-Do"
        #assert 'To-Do' in brower.title
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请她加入一个代办项
        inputbox =self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 
            'Enter a to-do item'
            )
        #在文本框输入”buy peacock feathers"
        # habit is fake flies fishing
        inputbox.send_keys('Buy peacock feathers')
        
        #按回车，页面更新
        #代办事项显示“1.buy peacock feathers"
        inputbox.send_keys(Keys.ENTER) 
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        
        #debug
        #print(self.browser.find_elements_by_id('id*'))
        #table = self.browser.find_element_by_id ("id_list_table")
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertTrue(
        #    any(row.text == '1: Buy peacock feathers' for row in rows) ,
        #    f"New to-do item did not appear in table. Contents were:\n {table.text}"
        #)
        #self.assertIn('1: Buy peacock feathers',[row.text for row in rows])

        #页面又显示一个文件框，可以输入其他代办事项
        #输入”use peacock feathers to make a fly“
        #time.sleep(1)
        inputbox =self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        #按回车，页面更新
        #代办事项显示“1.buy peacock feathers"
        inputbox.send_keys(Keys.ENTER) 
        #time.sleep(1)

        # reconstruct to function
        #self.check_for_row_in_list_table('1: Buy peacock feathers')
        #self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #self.fail('Finish the test')
        #按回车，页面更新
        #代办事项显示 2个代办项
        
        # 检查网站是否能记住她的清单
        # 看到网站为她生成了一个唯一的url
        # 并且网页有文字说明这个功能
        
        #访问这个url，发现代办事项还在。
        
        #满足的睡觉去了

    def test_can_start_a_list_at_different_urls(self):
        
        self.browser.get(self.live_server_url)
        
        #应用邀请她加入一个代办项
        inputbox =self.browser.find_element_by_id('id_new_item')
        #在文本框输入”buy peacock feathers"
        # habit is fake flies fishing
        inputbox.send_keys('Buy peacock feathers')
        
        #按回车，页面更新
        #代办事项显示“1.buy peacock feathers"
        inputbox.send_keys(Keys.ENTER) 
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+') 

        #页面又显示一个文件框，可以输入其他代办事项
        #输入”use peacock feathers to make a fly“
        inputbox =self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER) 
        #time.sleep(1)


        #按回车，页面更新
        #代办事项显示 2个代办项
        # reconstruct to function
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        
        # 检查网站是否能记住她的清单
        # 看到网站为她生成了一个唯一的url
        # 并且网页有文字说明这个功能
        
        #另一个叫Francis的新用户访问网站

        ##使用一个新浏览器会话
        ##确保Edith的信息不会从cookie中泄露出去
        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peachock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        #Francis create item
        inputbox =self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER) 
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis get unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url,'/list/.+') 
        self.assertNotEqual(francis_list_url,edith_list_url) 

        #在francis的页面里米有Edith的清单
        page_text = self.browser.find_elements_by_tag_name('body').text
        self.assertNotIn('Buy peachock feathers',page_text)
        self.assertNotIn('make a fly',page_text)
        #访问这个url，发现代办事项还在。
        
        #满足的睡觉去了
        
        
    #brower.quit()

# main can be removed for Django tests, no error if it is not removed.
#if __name__ == '__main__':
#    unittest.main()