def counting_vowels(text):  
    vowels = "aeiou"  
    quantity = 0  
 
    for letter in text.lower():  
        if letter in vowels:  
            quantity += 1  
 
    return quantity 