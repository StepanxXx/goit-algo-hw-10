"""
Module for optimizing manufacturing production of lemonade and fruit juice using linear programming.
"""
import pulp

# Ініціалізація моделі
model = pulp.LpProblem("maximize_manufacturing", pulp.LpMaximize)

lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('fruit_juice', lowBound=0, cat='Integer')

model += 2 * lemonade + fruit_juice <= 100 # Води
model += lemonade <= 50 # Цукру
model += lemonade <= 30 # Лимонного соку
model += 2 * fruit_juice <= 40 # Фруктового пюре

model += lemonade + fruit_juice

model.solve()

print("Виробляти лимонаду:", lemonade.varValue)
print("Виробляти фруктового соку:", fruit_juice.varValue)
print("Максимальна можлива загальна кількість вироблених",
    "продуктів \"Лимонад\" та \"Фруктовий сік\":", pulp.value(model.objective))
