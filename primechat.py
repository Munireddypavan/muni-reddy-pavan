def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

start_range, end_range = 1, 20

prime_numbers = []
for num in range(start_range, end_range + 1):
    if is_prime(num):
        prime_numbers.append(num)

print(f"Prime numbers between {start_range} and {end_range}: {prime_numbers}")
