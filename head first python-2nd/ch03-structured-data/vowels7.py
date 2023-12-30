vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("Provide a word to search for vowels: ")
for vowel in vowels.intersection(set(word)):
    print(vowel)
