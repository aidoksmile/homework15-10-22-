# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def FillArray():
    array = []
    array = [int(i) for i in input().split()]
    return array

def SumArrayEl(array):
    sum = 0
    for i in range(0, len(array)-1):
        if ((i + 1) % 2) == 0:
            sum = sum + int(array[i])
            print(array[i], end = ", ")
    return sum

print('Введите элементы массива через пробел: ')
array = FillArray()
print(f'сумма элементов на четных позициях = {SumArrayEl(array)} ')