#!/bin/bash

#grep Cheat Sheet

# ^ Matches the word at the beginning of the line

grep -i ^fruit /usr/share/dict/words


# $ Matches the word at the end of the line

grep -i cat$ /usr/share/dict/words

# . is a wildcard and will match any letter in string

grep -i s.ing /usr/share/dict/words