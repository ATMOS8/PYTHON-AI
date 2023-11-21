import re

def count_letter_v(poem):
    return len(re.findall(r'v', poem))

def remove_newlines(poem):
    return re.sub(r'\n', ' ', poem)

def replace_ch_co(poem):
    return re.sub(r'\b(ch|co)\b', lambda match: match.group().capitalize(), poem)

def replace_ai_hi(poem):
    return re.sub(r'\b(ai|hi)(.{3})', r'***', poem)

# Take input from the user
print("Enter your poem (press Enter twice to finish input):\n")
poem_lines = []
while True:
    line = input()
    if line:
        poem_lines.append(line)
    else:
        break

user_input = '\n'.join(poem_lines)

# Task 1: Count how many times 'v' appears in the poem
count_v = count_letter_v(user_input)
print(f"\nNumber of times 'v' appears: {count_v}")

# Task 2: Remove newlines from the poem
poem_without_newlines = remove_newlines(user_input)
print(f"\nPoem without newlines:\n{poem_without_newlines}")

# Task 3: Replace 'ch' or 'co' with 'Ch' or 'Co'
poem_with_replaced_ch_co = replace_ch_co(user_input)
print(f"\nPoem with replaced 'ch' or 'co':\n{poem_with_replaced_ch_co}")

# Task 4: Replace 'ai' or 'hi' followed by the next three characters with '*\*'
poem_with_replaced_ai_hi = replace_ai_hi(user_input)
print(f"\nPoem with replaced 'ai' or 'hi':\n{poem_with_replaced_ai_hi}")
