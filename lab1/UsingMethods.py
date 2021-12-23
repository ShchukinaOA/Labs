# Пробуем методы списков

first_list = ['п', 'р', 'и', 'в', 'е', 'т']
second_list = ['м', 'и', 'р']

print(first_list.index('и'))
print(second_list.count('и'))
first_list.insert(len(first_list) - 1, '!')
first_list.append('о')
first_list.extend(second_list)
print(first_list)
first_list.remove('и')
first_list.pop(0)
first_list.reverse()
print(first_list)
