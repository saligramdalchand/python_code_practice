#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:57:09 2018

@author: dc
"""

import webbrowser
import time
n = 0
while (n<4):
    time.sleep(1500)
    url1 = "https://www.youtube.com/watch?v=2L2lnxIcNmo"
    webbrowser.open_new(url1)
    time.sleep(1500)
    url2 = "https://www.youtube.com/watch?v=bkHuvrLxpUU"
    webbrowser.open_new(url2)
    n += 1