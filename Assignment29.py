def largest_prime_factor(n) :
    i = 2
    while i * i <= n :
        while n % i == 0 :
            n //= i
            max_prime = i
        i += 1
    if n > 1 :
        max_prime = n
    return max_prime
def sum_largest_prime_factors(start) :
    total_sum = 0
    for i in range(start, start + 9) :
        largest_prime = largest_prime_factor(i)
        total_sum += largest_prime
    return total_sum
start_number = int(input("Enter the starting number : "))
result = sum_largest_prime_factors(start_number)
print("The sum of largest prime factors for nine consecutive numbers is :", result)