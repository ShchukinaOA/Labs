from numpy import random
from typing import List

# Отсортировать список произвольных чисел по возрастанию и убыванию
def get_random_numbers():
    return [random.randint(-15, 15) for _ in range(10)]
numbers = get_random_numbers()

# Сортировка по возрастанию
asc_sorted = sorted(numbers)
# Сортировка по убыванию
desc_sorted = sorted(numbers, reverse=True)
# Вывод начального списка произвольных чисел
print('\nПроизвольные числа:', numbers)
# Вывод сначала по возрастанию, затем по убыванию
print('Отсортированный список произвольных чисел по возрастанию:', asc_sorted)
print('Отсортированный список произвольных чисел по убыванию:', desc_sorted)
