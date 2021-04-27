#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Prevent Screen Lock
import pyautogui
import time

while True:
    pyautogui.press('volumedown')
    time.sleep(1)
    pyautogui.press('volumeup')
    time.sleep(5)

