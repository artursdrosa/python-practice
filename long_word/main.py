from long_word_validator import long_word_validator

text = input("Enter the text: ")

long_words = long_word_validator(text)

if long_words:
    print("Long words found:")
    for word in long_words:
        print(word)
else:
    print("No long words found.")