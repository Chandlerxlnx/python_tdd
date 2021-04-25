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
        self.fail('Finish the test')
        #应用邀请她加入一个代办项
        
        #在文本框输入”buy peacock feathers"
        # habit is fake flies fishing
        
        #按回车，页面更新
        #代办事项显示“1.buy peacock feathers"
        
        #页面又显示一个文件框，可以输入其他代办事项
        #输入”use peacock feathers to make a fly“
        
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