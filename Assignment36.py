import random
def biased_coin_toss() :
    probability_of_head = 0.7
    result = "Head" if random.random() < probability_of_head else "Tail"
    return result
num_tosses = int(input("Enter the number of biased coin tosses : "))
head_count = 0
for _ in range(num_tosses) :
    result = biased_coin_toss()
    if result == "Head" :
        head_count += 1
print(f"Number of biased coin tosses : {num_tosses}")
print(f"Number of heads : {head_count}")
print(f"Number of tails : {num_tosses - head_count}")