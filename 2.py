# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def FillArray():
    array = []
    array = [int(i) for i in input().split()]
    return array

def MultArrayEl(array):
    l = len(array) // 2
    l = l if len(array) % 2 == 0 else l + 1
    second_array = []
    for i in range (l):
        second_array.append(array[i] * array[-i - 1])
    return second_array

print('Введите элементы массива через пробел: ')
array = FillArray()
print(f'Для списка {array} список произведений пар чисел =  {MultArrayEl(array)}')
