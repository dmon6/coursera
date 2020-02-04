#!/usr/bin/env python3.7

import csv

# List of lists
hosts = [['workstation.local', '192.168.25.46'],
         ['webserver.cloud', '10.2.5.6']]

# open file and write hosts to file
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
