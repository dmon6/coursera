#!/usr/bin/env python3.7

# This code checks whether or not a something in a directory is another directory or a file

import os

dir = os.getcwd()

for name in os.listdir('.'):
    full_name = os.path.join(dir, name)
    if os.path.isdir(full_name):
        print(f'{full_name} is a directory')
    else:
        print(f'{full_name} is a file')
