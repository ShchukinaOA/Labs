# Создать пустой словарь
empty_dict = {}

print(empty_dict)

# Создаем словарь о персоне, содержащий три пары «ключ: значение»
person = {
    'surname': 'Shchukina',
    'name': 'Olga',
    'age': '23',
}

print(person)

# Сгенерировать словарь, содержащий числа в роли ключей и квадраты чисел в роли значений.
def generate_dict():
    numbers = {}
    for i in range(2, 11):
        numbers[i] = i*i
    return numbers


numbers = generate_dict()
print(numbers)

# Опробовать печать значения из словаря по ключу.
print(person['surname'])
# Опробовать удаление элемента из словаря.
person.pop('name')
print(person)

# Опробовать методы словарей
nums_copy = numbers.copy()
print(person.get('age'))
print(nums_copy.keys())
print(nums_copy.values())

nums_copy.clear()
print(nums_copy)
print(person.popitem())

person.update({'nickname': 'Lelya'})
print(person)
