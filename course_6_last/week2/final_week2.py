#!/usr/bin/env python3
import requests
import os

user_ip = ''
url = 'http://' + ip + '/feedback'
files = [in_file for in_file in os.listdir('.') if '.txt' in in_file]
headers = ['title', 'name', 'date', 'feedback']

for item in files:
    with open(item) as f:
        d = {}
        for index, line in enumerate(f):
            d[headers[index]] = line.replace('\n', '')
    r = requests.post(url, json=d)
    if r.status_code != 201:
        print('Error code received: {}'.format(r.status_code))
        break
