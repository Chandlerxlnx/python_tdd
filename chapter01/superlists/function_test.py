# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:23:34 2021

@author: Chandler
"""

from selenium import webdriver

brower = webdriver.Firefox()
brower.get('http://localhost:8000')

assert 'Django' in brower.title