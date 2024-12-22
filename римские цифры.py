class Solution:
    def romanToInt(self, s: str) -> int:
        # Словарь, в котором хранятся римские символы и их значения
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        # Переменная для хранения результата
        result = 0
        
        # Проходим по всем символам строки
        for i in range(len(s)):
            # Если текущий символ меньше следующего, вычитаем его значение
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]
        
        return result
