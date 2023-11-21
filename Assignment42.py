def is_prime(num) :
    if num < 2 :
        return False
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0 :
            return False
    return True
def rotations_of_number(num) :
    num_str = str(num)
    rotations = [int(num_str[i:] + num_str[:i]) for i in range(len(num_str))]
    return rotations
def count_circular_primes(limit) :
    circular_primes = []
    for i in range(2, limit) :
        if all(is_prime(rot_num) for rot_num in rotations_of_number(i)) :
            circular_primes.append(i)
    return len(circular_primes)
limit_input = int(input("Enter the limit : "))
count = count_circular_primes(limit_input)
print(f"Number of circular primes below {limit_input} : {count}")