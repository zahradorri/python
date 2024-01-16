Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def count_character_frequency(sentence):
...     char_frequency = {}
...     for char in sentence:
...         if char.isalpha():
...             char = char.lower()
...             char_frequency[char] = char_frequency.get(char, 0) + 1
...     return char_frequency
... 
... input_sentence = input("Enter a sentence: ")
... result = count_character_frequency(input_sentence)
... 
... print("Character Frequencies:")
... for char, frequency in result.items():
...     print(f"{char}: {frequency}")
