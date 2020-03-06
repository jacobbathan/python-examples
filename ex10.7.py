# two words are anagrams if you can rearrange the letters from one to spell the other.
# write a function that takes two strings and returns True if anagrams

def is_anagram(word1, word2):
    first = sorted(word1.lower())
    second = sorted(word2.lower())
    if first == second:
        return True
    else:
        return False


print(is_anagram('listen', 'silent'))
print(is_anagram('evil', 'vale'))
print(is_anagram('debit card', 'bad credit'))
