"""
Module for Monte Carlo integration.
"""
import random

def is_inside(func, x, y):
    """Перевіряє, чи точка знаходиться всередині функції (під кривою)."""
    return y <= func(x)

def monte_carlo_calculation(func, a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(100000)]
        inside_points_count = 0
        for point in points:
            if is_inside(func, x=point[0], y=point[1]):
                inside_points_count += 1

        area_inside_part = inside_points_count / len(points)
        average_area += area_inside_part * a * b

    average_area /= num_experiments
    return average_area

if __name__ == "__main__":
    # Тестування функції
    WIDTH = 10
    HEIGHT = 5
    result = monte_carlo_calculation(lambda x: HEIGHT / WIDTH * x, WIDTH, HEIGHT, 100)
    print("Результат Монте-Карло:", result)
    print("Результат без Монте-Карло:", WIDTH * HEIGHT / 2)
