import task1
import task2

def main():
    while True:
        print("Виберіть завдання:")
        print("1. Оптимізація виробництва")
        print("2. Обчислення визначеного інтеграла методом Монте-Карло")
        print("3. Вихід")
        
        choice = input("Введіть номер завдання: ")
        
        if choice == '1':
            task1.optimize_production()
        elif choice == '2':
            task2.calculate_integral()
        elif choice == '3':
            print("Вихід з програми...")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
