def is_arguments_for_substr_correct(string, start_index, length):
    if length < 0:  # Условие 1: отрицательная длина подстроки
        return False

    if start_index < 0:  # Условие 2: отрицательный индекс
        return False

    if start_index >= len(string):  # Условие 3: индекс за границей строки
        return False
    
    if start_index + length > len(string):  # Условие 4: подстрока выходит за границу строки
        return False 
    
    return True  # Если ни одно из условий не выполнено, всё корректно

# Тестовые примеры
string = 'Sansa Stark'
print(is_arguments_for_substr_correct(string, 2, -3))   # => False
print(is_arguments_for_substr_correct(string, -1, 3))   # => False
print(is_arguments_for_substr_correct(string, 4, 100))  # => False
print(is_arguments_for_substr_correct(string, 10, 10))  # => False
print(is_arguments_for_substr_correct(string, 11, 1))   # => False
print(is_arguments_for_substr_correct(string, 3, 3))    # => True
print(is_arguments_for_substr_correct(string, 0, 5))    # => True 
