# two words are a reverse pair if each is a reverse of the other
# write a function that finds all the reverse pairs in the word list

from bisect import bisect


def find_pairs(list_of_words):
    for word in list_of_words:
        if word[::-1] in list_of_words:
            print(word, word[::-1]

            
