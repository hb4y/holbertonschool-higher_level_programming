#!/usr/bin/python3
word = "Holberton"
word_first_3 = "{:.2}".format(word)
word_last_2 = "{}".format(word[-2])
middle_word = "{:.7}".format(word[1:])
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
