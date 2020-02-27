#!/usr/bin/env python3.7
import re
from pprint import pprint
import csv
import operator

error = {}
per_user = {}

match_user = "([\w]*)\)$"
match_error_info = r"ticky: (INFO|ERROR) ([\w ]*) "

#match_error_info = r'.*(INFO|ERROR)\s+(.+)([\w.]+)'

with open('syslog.log') as f:
    for line in f:
        match = re.search(match_error_info, line)
        # print(match.group(2))
        if match:
            error_message = match.group(2)
            error[error_message] = error.get(error_message, 0) + 1
        user = re.search(match_user, line)
        username = user.group(1).replace(')', '')
        per_user[username] = per_user.get(username, {})
        if 'ERROR' in line:
            per_user[username]['ERROR'] = per_user[username].get(
                'ERROR', 0) + 1
        if 'INFO' in line:
            per_user[username]['INFO'] = per_user[username].get(
                'INFO', 0) + 1
# pprint(error)
# pprint(per_user)

# Sort dictionary
sorted_error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
sorted_per_user = sorted(per_user.items(), key=operator.itemgetter(0))

for item in sorted_per_user:
    if 'ERROR' in item[1].keys():
        pass
    else:
        item[1]['ERROR'] = 0
    if 'INFO' in item[1].keys():
        pass
    else:
        item[1]['INFO'] = 0

with open('error_message.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Error', 'Count'])
    for item in sorted_error:
        writer.writerow([item[0], item[1]])


with open('user_statistics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Username', 'INFO', 'ERROR'])
    for item in sorted_per_user:
        writer.writerow([item[0], item[1]['INFO'], item[1]['ERROR']])
