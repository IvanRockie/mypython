def is_contains_char(string, letter_for_look):
    index = 0
    while index < len(string):
        if string[index] == letter_for_look:
            return True 

        index += 1

    return False    

print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => False
print(is_contains_char('Awesomeness', 'm'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False
