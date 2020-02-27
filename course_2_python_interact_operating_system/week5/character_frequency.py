#!/usr/bin/env python3.7


def character_frequency(filename):
    """Counts the frequency of each character in the given file"""
    try:
        f = open(filename)
    except OSError:
        return None

    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters


sample = 'jsl;fkjweifjawihgjlnflajefnjhwjkhfawkejfh'


def char_count(text):
    characters = {}
    for char in text:
        characters[char] = characters.get(char, 0) + 1
    return characters


print(char_count(sample))
