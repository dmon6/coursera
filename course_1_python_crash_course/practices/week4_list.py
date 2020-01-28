#!/usr/bin/env python3.7

filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []

for filename in filenames:
    if '.hpp' in filename:
        newfilenames.append((filename, filename.replace('.hpp', '.h')))
    else:
        newfilenames.append((filename, filename))

print(newfilenames)


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for digits in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digits >= value:
                result += letter
                digits -= value
            else:
                result += '-'
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        say += word[1:] + word[0] + 'ay' + ' '
        # Turn the list back into a phrase
    return say.strip()


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))
