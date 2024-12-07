def vis_palindrome(word: str) -> bool: ##создает строку
    word = word.lower() ##приводим строку к нижнему регистру
    return word == word[::-1] ##проверяем Палиндром
def vis_not_palindrome(word: str) -> bool:##делаем то же самое только с отрицанием 
    return not vis_palindrome(word) ##делаем отрицание 

print(vis_palindrome('шалаш')) # true
print(vis_palindrome('хекслет')) # false
print(vis_palindrome('Довод')) # true
print(vis_palindrome('Функция')) # false

print(vis_not_palindrome('шалаш')) # false
print(vis_not_palindrome('Ага')) # false
print(vis_not_palindrome('хекслет')) # true
