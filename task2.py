import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def calculate_integral():
    # Визначення функції
    def f(x):
        return x ** 2

    # Межі інтегрування
    a = 0
    b = 2

    # Метод Монте-Карло для обчислення інтегралу
    def monte_carlo_integration(f, a, b, num_samples):
        x_samples = np.random.uniform(a, b, num_samples)
        y_samples = f(x_samples)
        integral = (b - a) * np.mean(y_samples)
        return integral

    # Обчислення інтегралу методом Монте-Карло
    num_samples = 10000
    monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)

    # Обчислення інтегралу за допомогою quad
    quad_result, quad_error = spi.quad(f, a, b)

    # Виведення результатів
    print("Метод Монте-Карло: ", monte_carlo_result)
    print("Метод quad: ", quad_result)

    # Побудова графіка функції
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

    # Побудова порівняльного графіка
    methods = ['Monte Carlo', 'Quad']
    results = [monte_carlo_result, quad_result]

    fig, ax = plt.subplots()
    ax.bar(methods, results, color=['blue', 'green'])
    ax.set_ylabel('Інтеграл')
    ax.set_title('Порівняння результатів обчислення інтегралу')
    plt.show()

if __name__ == "__main__":
    calculate_integral()
