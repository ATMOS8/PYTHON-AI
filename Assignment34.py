def encrypt_sentence(message) :
    def reverse_word(word) :
        return word[::-1]
    def rearrange_word(word) :
        vowels = "aeiouAEIOU"
        consonants = ""
        for letter in word :
            if letter not in vowels :
                consonants += letter
        vowels_in_word = [char for char in word if char in vowels]
        return ''.join([consonants, ''.join(vowels_in_word)])
    words = message.split()
    encrypted_message = ""
    for i, word in enumerate(words, 1) :
        if i % 2 == 0 :
            encrypted_message += rearrange_word(word) + " "
        else :
            encrypted_message += reverse_word(word) + " "
    return encrypted_message.strip()
user_input = input("Enter a message : ")
result = encrypt_sentence(user_input)
print("The encrypted message is : ", result)