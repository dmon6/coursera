import subprocess

# Basic way to do rsync in python
src = "<source-path>" 
dest = "<destination-path>"
subprocess.call(["rsync", "-arq", src, dest])

