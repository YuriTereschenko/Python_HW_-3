#  Найти НОК двух чисел

def find_nok(a, b):
    if b > a:
        temp_b = a
        temp_a = b
    else:
        temp_b = b
        temp_a = a
    while True:
        if temp_a % temp_b == 0:
            return (a*b)/temp_b
        else:
            temp = temp_a % temp_b
            temp_a = temp_b
            temp_b = temp


print(find_nok(32, 20))
