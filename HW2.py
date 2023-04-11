# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
#пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# from math import *
# n = int (input())
# a=0
# for a in range(1,n+1):
#     a=a+1
#     a=factorial(a)
# print(a)

#Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
# print('x y z a')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             a=not(x or y)and z
#             if a==True:
#                 a=1
#             if a==False:
#                 a=0
#             print(x,y,z,a)

#Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
#«one» «onetwonine» - o – 2, n – 3, e – 2
# a = 'kllkflkfgnlrekgn'
# b = 'kl'
# print(a.count(b))


#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
n = int(input())
n=[abs(n)]
for num in range(-n, n + 1):
    length = len(n)
    a = n[length-1]
    for i in range(length-1, -1,-1):
       n[i] = n[i-1]
    n[0] = a
print(n)


