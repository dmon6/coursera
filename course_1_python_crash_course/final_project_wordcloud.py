#!/usr/bin/env python3.7

'''
1. Get input file(big ass string to input to wordcloud to make a pretty picture)
2. Create a dictionary of words and their frequency within their text
	- Filter out uninteresting words ['if', 'a', 'the', 'of'] and so on
	- Filter out the punctuation
3. pipenv --python 3.7
		pipenv install wordcloud
4. wordcloud - generate word cloud image:
		cloud = wordcloud.WordCloud()
		cloud.generate_from_frequencies(frequencies)
		cloud.to_file("my_file.jpg")

'''

import wordcloud
from pprint import pprint
from string import punctuation

common_words = ['they', 'then', 'that', 'with', 'from', 'when', 'this']

with open('text_file_kama.txt') as f:
    data = f.read()

word_count = {}
example = 'dennis monton is dennis dennis but butt typing up some stuff because i had to'

# for word in example.split():
#     if word not in word_count:
#         word_count[word] = 1
#     else:
#         word_count[word] += 1

# pprint(word_count)

for word in data.replace('\n', ' ').split(' '):
    new_word = ''.join([x for x in word.strip(
        punctuation) if x.isalpha()]).lower()
    if len(new_word) > 3:
        if new_word not in word_count:
            word_count[new_word] = 1
        else:
            word_count[new_word] += 1
    else:
        pass

for k, v in word_count.items():
    if v > 30:
        print(f'Word: {k}\t|| Frequency: {v}')

# cloud = wordcloud.WordCloud()
# cloud.generate_from_frequencies(word_count)
# cloud.to_file("my_file.jpg")
