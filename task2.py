#  Вычислить число Пи c заданной точностью (я так понимаю здесь имелось ввиду "выведите" иначе очень странное задание)
#  Пример: при d = 0.001,  c= 3.141 (судя по всему без округления... какой практический смысл?)
import math

d = 0.001


def accuracy(num):  # Не стал добавлять проверку на положительно или отрицательное число
    temp = num
    count = 0
    while temp < 1:
        temp *= 10
        count += 1
    print(count)
    return count


result1 = round(math.pi, accuracy(d))  # Это если нужно адекватно с округением
result2 = str(math.pi)
result2 = float(result2[0:(accuracy(d)+2)])  # Это второй вариант, если нам нужно без округления
print(result2)
