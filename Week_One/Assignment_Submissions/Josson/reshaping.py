# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-btSsrIXrpm_BkKp3ltdTq6RjXob8gAa
"""

import numpy as np
print("Enter m,n and numbers of array")
x = [int(x) for x in input("Enter values ").split()]
a = np.array(x[2:])
m = x[0]
n = x[1]
print(a.reshape(m, n))



