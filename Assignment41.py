def word_with_max_frequency(text) :
    words = text.lower().split()
    word_count = {}
    for word in words :
        if word in word_count :
            word_count[word] += 1
        else :
            word_count[word] = 1
    max_frequency = 0
    max_frequency_words = []
    for word, count in word_count.items() :
        if count > max_frequency :
            max_frequency = count
            max_frequency_words = [word]
        elif count == max_frequency :
            max_frequency_words.append(word)
    max_length_word = max(max_frequency_words, key=lambda w : (len(w), w))
    return f"{max_length_word} {max_frequency}"
text_input = input("Enter text : ")
result = word_with_max_frequency(text_input)
print("Word with maximum frequency and its count : ", result)