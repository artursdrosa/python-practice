def long_word_validator(text):
    long_word = []

    for word in text.split():
        if len(word) > 10:
            long_word.append(word)
    
    return long_word