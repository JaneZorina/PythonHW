#Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# import random
# num=[random.randint(1, 10)for i in range(7)]
# print(num)
# num_2=filter(lambda x:x>5,num)
# num_2=list(num_2)
# print(num_2)

#Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
#[1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.


num=[1, 5, 2, 3, 4, 6, 1, 7]
print(num)
def get_num_2(num):
    num_2 = [num[0]]
    for i in num:
        if i > max(num_2):
            num_2.append(i)
    return num_2
print(get_num_2(num))

#Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
#[1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают.Список уникальных элементов [1, 4, 2, 3, 6, 7]
# import random
# num=[random.randint(1, 10)for i in range(7)]
# a=len(num)
# print(num)
# num_2=set(num)
# b=len(num_2)
# print (f'Список уникальных элементов {list(num_2)}')
# print(f'{a-b} элемента совпадают')



