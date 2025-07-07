sentence = input("Enter a sentence: ")

char_count = len(sentence)
print("Number of characters:", char_count)
print("Uppercase:", sentence.upper())

print("Lowercase:", sentence.lower())

print("Spaces replaced with underscores:", sentence.replace(" ", "_"))
if 'Python' in sentence:
    print("The word 'Python' is in the sentence.")
else:
    print("The word 'Python' is NOT in the sentence.")

