import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определение функции по изображению
def f(x1, x2):
    numerator = np.sin(x1**2 - x2**2)**2 - 0.5
    denominator = (1 + 0.001*(x1**2 + x2**2))**2
    return 0.5 + numerator / denominator

# Параметры по заданию
x1_range = (-2.0, 2.0)
x2_range = (-2.0, 2.0)
test_point = (0.0, 0.0)  # (x10, x20)

# Создание данных
x1 = np.linspace(x1_range[0], x1_range[1], 400)
x2 = np.linspace(x2_range[0], x2_range[1], 400)
X1, X2 = np.meshgrid(x1, x2)
Z = f(X1, X2)

# Вычисление значения в тестовой точке
x10, x20 = test_point
z0 = f(x10, x20)

# Создание фигуры с 4 подграфиками
fig = plt.figure(figsize=(14, 10))
fig.suptitle(f"Визуализация функции f(x₁, x₂)\nТестовая точка: ({x10}, {x20}) - Значение: {z0:.4f}", 
             fontsize=14, y=1.02)

# 1. 3D поверхность в изометрии
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
surf = ax1.plot_surface(X1, X2, Z, cmap='viridis', edgecolor='none')
ax1.set_title("1. 3D поверхность (изометрия)")
ax1.set_xlabel("x₁")
ax1.set_ylabel("x₂")
ax1.set_zlabel("y = f(x₁, x₂)")
ax1.scatter([x10], [x20], [z0], color='red', s=50)
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=5, label='Значение функции')

# 2. Вид сверху (контурный график)
ax2 = fig.add_subplot(2, 2, 2)
contour = ax2.contourf(X1, X2, Z, levels=20, cmap='viridis')
ax2.set_title("2. Вид сверху (контуры)")
ax2.set_xlabel("x₁")
ax2.set_ylabel("x₂")
ax2.plot(x10, x20, 'ro')  # Тестовая точка
fig.colorbar(contour, ax=ax2, shrink=0.5, aspect=5, label='Значение функции')

# 3. Сечение при x₂ = x20
ax3 = fig.add_subplot(2, 2, 3)
x1_line = np.linspace(x1_range[0], x1_range[1], 400)
z_line1 = f(x1_line, x20)
ax3.plot(x1_line, z_line1, 'b-', linewidth=2)
ax3.set_title(f"3. Сечение f(x₁, x₂={x20})")
ax3.set_xlabel("x₁")
ax3.set_ylabel("y = f(x₁, x₂)")
ax3.grid(True)
ax3.plot(x10, z0, 'ro')  # Тестовая точка

# 4. Сечение при x₁ = x10
ax4 = fig.add_subplot(2, 2, 4)
x2_line = np.linspace(x2_range[0], x2_range[1], 400)
z_line2 = f(x10, x2_line)
ax4.plot(x2_line, z_line2, 'g-', linewidth=2)
ax4.set_title(f"4. Сечение f(x₁={x10}, x₂)")
ax4.set_xlabel("x₂")
ax4.set_ylabel("y = f(x₁, x₂)")
ax4.grid(True)
ax4.plot(x20, z0, 'ro')  # Тестовая точка

plt.tight_layout()
plt.show()