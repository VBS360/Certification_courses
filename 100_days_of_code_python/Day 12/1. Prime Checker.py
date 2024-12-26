num = int(input("Enter the number you want to check.: "))

def prime_checker():
    if num > 1:
        for digit in range (2, int(num**0.5)+1):
            if num % digit == 0:
                return False
            return True
    else:
        return False

print(prime_checker())
