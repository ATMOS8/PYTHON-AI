def find_more_than_average(list_of_marks):
    avg_mark = sum(list_of_marks) / len(list_of_marks)
    above_average_count = len([mark for mark in list_of_marks if mark > avg_mark])
    return (above_average_count / len(list_of_marks)) * 100
def generate_frequency(list_of_marks):
    max_mark = max(list_of_marks)
    frequency = [0] * (max_mark + 1)
    for mark in list_of_marks:
        frequency[mark] += 1
    return frequency
def sort_marks(list_of_marks):
    return sorted(list_of_marks)
input_marks = input("Enter the marks of 10 students (comma-separated, e.g., 12,18,25,24,2,5,18,20,20,21): ")
list_of_marks = [int(mark) for mark in input_marks.split(",")]
more_than_average = find_more_than_average(list_of_marks)
frequency = generate_frequency(list_of_marks)
sorted_marks = sort_marks(list_of_marks)
print(f"Percentage of students who scored more than the average: {more_than_average}%")
print("Frequency of marks:", frequency)
print("Sorted marks:", sorted_marks)