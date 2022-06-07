# Разложите число неа простые множители

def prime_factors(num):
    simple = [2, 3, 5, 7]
    result = []
    for i in simple:
        while num % i == 0 and num > 0:
            num /= i
            result.append(i)
    if num > 1:
        result.append(num)
    return result


print(prime_factors(1050))
