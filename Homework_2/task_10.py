# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0 
# 2

n = int(input('Введите кол-во монет: '))
count0 = 0
count1 = 0
min = 0
for i in range(n):
    a = int(input('Введите сторону монеты (орёл - 0 / решка - 1): '))
    if a == 0:
        count0 += 1
    else:
        count1 += 1
if count0 < count1:
    min = count0
else:
    min = count1
print(f' Необходимо перевернуть {min} монет(у/ы)')