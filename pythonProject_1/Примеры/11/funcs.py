def is_prime_number(number):
    for digit in range(2, int(number ** .5) + 1):
        if number % digit == 0:
            return False
    return True


prime_numbers = [num for num in range(1, 102) if is_prime_number(num)]

print(prime_numbers)

