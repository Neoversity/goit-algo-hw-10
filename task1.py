import pulp
import matplotlib.pyplot as plt

def optimize_production():
    # Створюємо модель задачі
    model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

    # Змінні
    lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
    fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

    # Обмеження ресурсів
    model += 2 * lemonade + fruit_juice <= 100  # Обмеження на воду
    model += 1 * lemonade <= 50  # Обмеження на цукор
    model += 1 * lemonade <= 30  # Обмеження на лимонний сік
    model += 2 * fruit_juice <= 40  # Обмеження на фруктове пюре

    # Цільова функція
    model += lemonade + fruit_juice, "Total Production"

    # Розв'язання задачі
    model.solve()

    # Виведення результатів
    lemonade_produced = pulp.value(lemonade)
    fruit_juice_produced = pulp.value(fruit_juice)
    total_production = lemonade_produced + fruit_juice_produced

    print(f"Лимонад: {lemonade_produced}")
    print(f"Фруктовий сік: {fruit_juice_produced}")
    print(f"Загальна кількість вироблених продуктів: {total_production}")

    # Візуалізація результатів
    products = ['Lemonade', 'Fruit Juice']
    quantities = [lemonade_produced, fruit_juice_produced]

    plt.figure(figsize=(10, 6))
    plt.bar(products, quantities, color=['yellow', 'orange'])
    plt.xlabel('Продукти')
    plt.ylabel('Кількість')
    plt.title('Максимальне виробництво продуктів')
    plt.show()

if __name__ == "__main__":
    optimize_production()
