#!/usr/bin/env python3.7

import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True)
print(result.stdout.decode())
