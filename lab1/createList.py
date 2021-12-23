from typing import List
# Cписок символов из строки
def get_list_of_letters(string: str) -> List[str]:
    array_letters = []
    for letter in string:
        array_letters.extend(letter)
    return array_letters
list = get_list_of_letters('тестовая строка')
print(list)
# Вывести пустой список
empty_list = []
print(empty_list)
