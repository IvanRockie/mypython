def my_substr(string, length):
    result = ''
    index = 0

    while index < length and index < len(string):
        current_char = string[index]
        result = result + current_char
        index = index + 1

    return result

# Тесты
print(my_substr('fjjsahhdf', 1))  # => 'f'
print(my_substr('fjdjjfjdf', 7))  # => 'fjdjjfj'
