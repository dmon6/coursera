#!/bin/bash
# Some helpful bits from the video

cat capitalize.py
# OUTPUT
##!/usr/bin/env python3.7
#import sys
#
#for line in sys.stdin:
#    print(line.strip().capitalize())

cat haiku.txt
# OUTPUT
# advance your career,
# automating with Python
# it's so fun to learn.

cat haiku.txt | ./capitalize.py
# OUTPUT
# Advance your career,
# Automating with Python,
# It's so fun to learn. 

./capitalize.py < haiku.txt
# OUTPUT
# Advance your career,
# Automating with Python,
# It's so fun to learn. 


#Count Number of processes in var log to see which is using most CPU
cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr |head
