def run_length_encoding(input_string) :
    if not input_string :
        return ""
    encoded_string = ""
    count = 1
    for i in range(1, len(input_string)) :
        if input_string[i] == input_string[i - 1] :
            count += 1
        else :
            encoded_string += str(count) + input_string[i - 1]
            count = 1
    encoded_string += str(count) + input_string[-1]
    return encoded_string
input_string = input("Enter a string to perform run-length encoding : ")
encoded_result = run_length_encoding(input_string)
print("Run-length encoded string :", encoded_result)