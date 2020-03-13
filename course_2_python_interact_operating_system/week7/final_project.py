#!/usr/bin/env python3.7
import re

# Exercise 1
line_info = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
line_error = "May 27 11:45:40 ubuntu.local ticky: ERROR: Created ticket [#1234] (username)"
line_user = "Jan 31 14:56:35 ubuntu.local ticky: ERROR Tried to add information to closed ticket (noel)"

info_re = re.search(r"ticky: INFO: ([\w ]*) ", line_info)
error_re = re.search(r"ticky: ERROR: ([\w ]*) ", line_error)
user_re = re.search(r"(\([\w]*\))$", line_user)


print(info_re.group(1))
print(error_re)
print(user_re)


# Exercise 2
import operator

# example dictionary
fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}

# sort items in dictionary using operator module
# sort items based on dictionary keys
sorted(fruit.items(), key=operator.itemgetter(0))

# sort items based on dictionary values
sorted(fruit.items(), key=operator.itemgetter(1))

# you can sort in reverse as well
print(sorted(fruit.items(), key=operator.itemgetter(1), reverse=True))


# Lab portion
import re

error = {}
per_user = 	{}

match_user = "([\w]*)\)$"
match_error = re.search(r"ticky: ERROR ([\w ]*) ", line_error)

with open(file) as f:
	for line in f:
		match = re.search(match_error, line)
		if match:
			error_message = match.group(1)
			error[error_message] = error.get(error_message, 0) + 1
		user = re.search(match_user, line)
		if user:
			username = user.group(1).replace(')', '')