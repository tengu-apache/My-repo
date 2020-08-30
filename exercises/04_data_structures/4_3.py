#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:14:56 2020

@author: python
"""

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
commands = config.split()
vlans = commands[-1].split(',')
print(vlans)
