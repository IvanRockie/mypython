import random
results = []
results_second = []
time_right = 0
time_not_right = 0
for i in range(1000):
  result = random.choice([1,2,3,4,5,6,7,8,9,10])
  result_second = random.choice([1,2,3,4,5,6,7,8,9,10])
  results.append(result)
  results_second.append(result_second)
  if result == result_second:
    time_right += 1

sum_of_the_rows = [a + b for a, b in zip(results, results_second)] 
numbers_to_count = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
times_numbers = {num: sum_of_the_rows.count(num) for num in numbers_to_count}
print(time_right)
