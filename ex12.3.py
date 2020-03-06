# write a function called most_frequent that takes a string
# and prints the letters in decreasing order of frequency

def make_dictionary(string):
    dictionary = {}
    for letter in string:
        dictionary[letter] = 1 + dictionary.get(letter, 0)

    return dictionary

def most_frequent(string):
    letters = [letter.lower() for letter in string]
    dictionary = make_dictionary(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print(letter, count)


text = 'The rain in Spain falls mainly on the plain'
text2 = 'Det er bedre å putte melkekartongen i restavfallet enn i papirgjenvinningen ut fra de forutsetningen som er med i beregningene, sier Christian Solli, miljøsystemanalytiker i Asplan Viak AS. Melkekartonger som kastes i restavfallet går til energigjenvinning i fjernvarmeanlegg.'
most_frequent(text)
most_frequent(text2)
