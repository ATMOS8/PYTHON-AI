def sms_encoding(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()
    abbreviated_sentence = []
    for word in words:
        encoded_word = ''
        has_consonant = any(letter for letter in word if letter not in vowels)
        if has_consonant:
            encoded_word = ''.join([char for char in word if char not in vowels])
        else:
            encoded_word = word
        abbreviated_sentence.append(encoded_word)
    return ' '.join(abbreviated_sentence)
user_input = input("Enter a sentence: ")
result = sms_encoding(user_input)
print("The abbreviated sentence for SMS is:", result)