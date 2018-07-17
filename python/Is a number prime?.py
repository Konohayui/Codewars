def is_prime(num):
    if num != 2 and num % 2 == 0:
        return False
    elif num < 2:
        return False
    else:
        for n in range(2, int((num)**(0.5)) + 1):
            if num % n == 0:
                return False
        return True
