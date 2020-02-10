#!/usr/bin/env python3.7

import re

# Split practice
# check for ending punctuation
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
# output:
# ['One sentence', ' Another one', ' And the last one', '']

# Includes ending punctuation plus the split of the sentence
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
# output:
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']
print('')
# Sub practice
print(re.sub(r"[\w.%t-]+@[\w.-]+", "[REDACTED]",
             "Just got an email from dennismonton@yahoo.com"))

print('')
# From Practice on video - Creates groups from phone nunber and inputs them into passed string


def convert_phone_number(phone):
    result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
    return result


# My number is (212) 345-9999.
print(convert_phone_number("My number is 212-345-9999."))
# Please call (888) 555-1234
print(convert_phone_number("Please call 888-555-1234"))
print(convert_phone_number("123-123-12345"))  # 123-123-12345
# Phone number of Buckingham Palace is +44 303 123 7300
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))

print('')
# Example using more back references from video
name_last = 'Monton, Dennis'
print(f'This is the variable name_last: {name_last}')
print('Transforming it with re.sub')
print(re.sub(r"([\w .-]*), ([\w .-]*)$", r"\2 \1", name_last))
