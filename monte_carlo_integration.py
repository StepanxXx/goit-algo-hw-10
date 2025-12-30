"""
This module performs Monte Carlo integration for a specific function and
visualizes the results.
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

from monte_carlo_calc import monte_carlo_calculation


# Визначення функції та межі інтегрування
def f(x_range):
    """
    Computes the square of the input x.
    """
    return x_range ** 2

A = 0  # Нижня межа
B = 2  # Верхня межа

integral, error = spi.quad(f, A, B)
print("Інтеграл: ", integral, error)

average_area = monte_carlo_calculation(f, B, f(B), 100)
print("Середня площа за 100 експериментів методом Монте-Карло: ", average_area)




# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(A, B)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=A, color='gray', linestyle='--')
ax.axvline(x=B, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(A) + ' до ' + str(B))
plt.grid()
plt.show()
