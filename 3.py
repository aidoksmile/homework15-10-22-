#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def FillArray():
    array = []
    array = [float(i) for i in input().split()]
    return array

def Max_Min(array):
    l = len(array)
    second_array = []
    for i in range (l):
        second_array.append(round(array[i] % 1, 10))
    res = max(second_array) - min(second_array)
    return res

print('Введите элементы массива через пробел: ')
array = FillArray()
print(Max_Min(array))