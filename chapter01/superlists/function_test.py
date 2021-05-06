# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:23:34 2021

@author: Chandler
"""

from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        self.browser.get('http://localhost:8000')
        
        #网页应该包含“to-Do"
        #assert 'To-Do' in brower.title
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').header_text
        self.assertIn('To-Do',header_text)

        #应用邀请她加入一个代办项
        inputbox =self.browser.find_element_by_id('id_new-item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 
            'Enter a to-do item'
            )
        #在文本框输入”buy peacock feathers"
        # habit is fake flies fishing
        inputbox.send_keys('buy peacock features')
        
        #按回车，页面更新
        #代办事项显示“1.buy peacock feathers"
        inputbox.send_keys(keys.ENTER) 
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        #页面又显示一个文件框，可以输入其他代办事项
        #输入”use peacock feathers to make a fly“
        
        self.fail('Finish the test')
        #按回车，页面更新
        #代办事项显示 2个代办项
        
        # 检查网站是否能记住她的清单
        # 看到网站为她生成了一个唯一的url
        # 并且网页有文字说明这个功能
        
        #访问这个url，发现代办事项还在。
        
        #满足的睡觉去了
        
    #brower.quit()

if __name__ == '__main__':
    unittest.main()