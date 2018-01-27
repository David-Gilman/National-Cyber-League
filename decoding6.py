import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


for i in range(1, 1829):
	for j in range(1, 1829):
		if is_prime(i) and is_prime(j):
			if i * j == 1829:
				print(i)
				print(j)


