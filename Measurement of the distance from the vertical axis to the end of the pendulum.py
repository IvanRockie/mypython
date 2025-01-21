from sympy.solvers import solve
from sympy import Symbol
import math
for i in range(100):
  L = 20 / 100
  g = 9.81
  t = i
  theta_0_deg = 30 
  pi = math.pi
  first_t = 2*pi*((L/g)**(1/2))
  first_n = t/first_t
  theta_0_rad = math.radians(theta_0_deg)
  #угол отклонения в момент t
  theta_t_rad = theta_0_rad * math.cos((2 * pi / first_t) * t)
  #горизонтальное расстояние
  gorisontal = L * math.sin(theta_t_rad)
  gorisontal_cm = gorisontal * 100
  path = L * theta_t_rad ...................................
  path_cm = path * 100
  print(f"Путь, пройденный маятником за {t} секунд: {path_cm:.2f} см")
  print(f"Время {t} с: {gorisontal_cm:.2f} см")
