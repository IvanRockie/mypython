import random
import numpy as np  
import matplotlib.pyplot as plt
import math

furie_arr = []
array = [random.randint(-5, 5) for _ in range(1000)]
X = np.fft.fft(array)
furie_arr.append(X)
amplitude = np.abs(X)
frequency = np.fft.fftfreq(len(array), 1) 

plt.figure(figsize=(20, 12))
plt.plot(frequency[:len(frequency)//2], amplitude[:len(frequency)//2])
plt.title("Быстрое преобразование Фурье (БПФ)")
plt.xlabel("Частота")
plt.ylabel("Амплитуда")
plt.grid(True)
plt.show() 
# Второй график
x_values = range(1000)  
y_values = []
for x in x_values:
    angle = 32 * math.pi
    sin_graf = (math.sin(x) * angle) / 1000
    y_values.append(sin_graf)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='sin_graf')

plt.title("График функции")
plt.xlabel("x")
plt.ylabel("sin_graf")
plt.grid(True)  
plt.legend()
plt.show()
