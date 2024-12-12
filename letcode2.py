class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # Подсчитываем количество символов в строках s и target
        s_count = Counter(s)
        target_count = Counter(target)
        
        # Инициализация переменной для подсчета числа перестановок
        result = float('inf')  # Начальное значение - очень большое число
        
        # Проверяем, сколько раз можно составить target из s
        for char in target_count:
            if char not in s_count:  # Если символ в target отсутствует в s
                return 0
            # Считаем, сколько раз можем использовать символы из s
            result = min(result, s_count[char] // target_count[char])
        
        return result
