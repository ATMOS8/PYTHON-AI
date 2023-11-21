def find_smallest_number(n) :
    try:
        if n <= 0 :
            return "Number of divisors should be a positive integer."
        def count_divisors(num) :
            count = 0
            for i in range(1, int(num ** 0.5) + 1) :
                if num % i == 0 :
                    if num // i == i :
                        count += 1
                    else :
                        count += 2
            return count
        smallest_num = 1
        div_count = 1
        while True :
            if count_divisors(smallest_num) == n :
                return smallest_num
            smallest_num += 1
    except Exception as e :
        return f"Error : {e}"
num_divisors = int(input("Enter the number of divisors : "))
result = find_smallest_number(num_divisors)
print(f"The smallest number with {num_divisors} divisors is :", result)