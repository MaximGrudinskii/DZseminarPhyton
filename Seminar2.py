# 1. По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# 3! = 1 * 2 * 3

# n = int(input('Введите число: '))
# b= n
# result = 1
# while n > 0:
#     result*=n
#     n-=1
# print(f'Ответ -> {b}! = {result}')

# 2. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# 1 1 2 3 5 8
# 5 -> 5
# 8 -> 6
# 7 -> -1

# n = int(input('n: '))
# f_1 = 1
# f_2 = 1
# count = 2

# while f_2 < n:
#     count += 1
#     f_1, f_2 = f_2, f_1 + f_2
    
# if f_2 == n:
#     print(count)
# else:
#     print(-1)
    
# print(count if f_2 == n else -1)

# n = int(input('n: '))
# f_1 = 1
# f_2 = 1
# count = 2

# while f_2 <= n:
#     if f_2 == n:
#         print(count)
#         break
#     count += 1
#     f_1, f_2 = f_2, f_1 + f_2
# else:
#     print(-1)

# 1. Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики 
# за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов 
# Цельсия. Напишите программу, помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел.

# Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50


# days = int(input('Days: '))
# count = 0
# max_count = 0
# for i in range(days):
#     temp = int(input('temp: '))
#     if temp > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
# print(max_count)

# range(5) -> 0, 1, 2, 3, 4
# len() -> возвращает количество элементов в коллекци
# range(5) -> 0, 1, 2, 3, 4
# range(5, 11) -> 5, 6, 7, 8, 9, 10
# range(1, 11, 2) -> 1, 3, 5, 7, 9

# days = int(input('Days: '))
# days_list = []
# for i in range(days):
#     temp = int(input('temp: '))
#     days_list.append(temp)

# count = 0
# max_count = 0
# for i in range(len(days_list)):
#     if days_list[i] > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
# print(max_count)