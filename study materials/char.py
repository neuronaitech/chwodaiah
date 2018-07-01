# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:05:28 2018

@author: nandavari
"""

import re
c=input("enter data:")
re.sub('.',lambda m: {'b':'v','v':'b'}.get(m.group(), m.group()), c)
