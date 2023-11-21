def find_correct(word_dict) :
    correct_count = 0
    almost_correct_count = 0
    wrong_count = 0
    for correct_word, contestant_word in word_dict.items() :
        if correct_word == contestant_word :
            correct_count += 1
        else :
            if len(correct_word) != len(contestant_word) :
                wrong_count += 1
            else :
                differences = sum(c1 != c2 for c1, c2 in zip(correct_word, contestant_word))
                if differences <= 2 :
                    almost_correct_count += 1
                else :
                    wrong_count += 1
    return [correct_count, almost_correct_count, wrong_count]
user_dict = {}
num_pairs = int(input("Enter the number of word pairs : "))
for _ in range(num_pairs) :
    correct_word = input("Enter the correct word : ")
    contestant_word = input("Enter the contestant's spelling : ")
    user_dict[correct_word] = contestant_word
result = find_correct(user_dict)
print("The count of correct, almost correct, and wrong answers are : ", result)