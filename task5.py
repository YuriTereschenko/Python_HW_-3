# Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.

with open("t5_text.txt", 'r') as data:
    result = data.read()
    data.close()
result = result.split()
to_del = []

for i in range(0, len(result)):
    result[i] = int(result[i])
    if result[i] % 2 == 0:
        to_del.append(result[i])

for j in to_del:
    result.remove(j)

with open("t5_text.txt", 'w') as dt:
    for i in result:
        dt.write(f"{i}\t")
    dt.close()
