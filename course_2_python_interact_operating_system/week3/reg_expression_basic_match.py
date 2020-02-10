#!/usr/bin/env python3.7

import re

log = 'July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade'
regex = r"\[(\d+)\]"
result = re.search(regex, log)

print(result)


# Match beginning and end of string example
text = 'Denied'
r = re.search(r"^d.*d$", text)

print(r)


def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"


print(rearrange_name('Monton, Dennis J.'))
