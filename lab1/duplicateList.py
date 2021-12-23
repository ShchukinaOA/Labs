from typing import List
# Список символов строки, повторенных 2 раза
def get_duplicated_letters_list(string: str) -> List[str]:
    array_letters = []
    for letter in string:
        array_letters.append(letter*2)
    return array_letters
    
list_of_letters = get_duplicated_letters_list('Щукина')

# Вывод списка символов строки, повторенных 2 раза
print(list_of_letters)
