def is_prime(number):
    if number > 1:
        for digit in range (2,int(number**0.5) + 1):
            if number % digit == 0:
                return False
        return True
    else:
        return False

is_prime (75)
print(is_prime(75))