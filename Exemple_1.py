"""
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел A. 
Последняя строка содержит число X
"""

def check_input(massege):

    num = input(massege)

    is_correct = False
    while(is_correct == False):
        if (num.isdigit()):
            if(0 < int(num)):
                is_correct = True
            else:
                print('Похоже вы ввели не число\n')
                num = input(massege)
        else:
            print('Упс :(\n Вы ввели не число, а что-то другое\n')
            num = input(massege)
    return num

N = int(check_input("Введите количество элементов в массиве\n"))
table = list()

for i in range(N):
    x = int(check_input(f"Введите значение массива под номером {i + 1}\n"))
    table.append(x)

X = int(check_input("Введите число, которое хотите посчитать\n"))
count = 0

for i in range(N):
    if(table[i] == X):
        count += 1

print(f"Числа {X} встречаеться {count} раз")