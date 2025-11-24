#!/usr/bin/env python3
"""
Простой консольный калькулятор на Python
"""

class Calculator:
    """Класс калькулятора с базовыми операциями"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Сложение двух чисел"""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Вычитание двух чисел"""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Умножение двух чисел"""
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Деление двух чисел"""
        if b == 0:
            raise ValueError("Ошибка: Деление на ноль невозможно!")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
        return result
    
    def _add_to_history(self, operation):
        """Добавляет операцию в историю"""
        self.history.append(operation)
        # Ограничиваем историю последними 10 операциями
        if len(self.history) > 10:
            self.history.pop(0)
    
    def show_history(self):
        """Показывает историю операций"""
        if not self.history:
            print("История операций пуста")
            return
        
        print("\n" + "="*40)
        print("📊 ИСТОРИЯ ОПЕРАЦИЙ:")
        print("="*40)
        for i, operation in enumerate(self.history, 1):
            print(f"{i}. {operation}")
        print("="*40)

def display_menu():
    """Отображает меню калькулятора"""
    print("\n" + "🎯 ДОСТУПНЫЕ ОПЕРАЦИИ:")
    print("1. ➕ Сложение")
    print("2. ➖ Вычитание") 
    print("3. ✖️ Умножение")
    print("4. ➗ Деление")
    print("5. 📊 Показать историю")
    print("6. 🚪 Выход")
    print("-" * 30)

def get_number(prompt):
    """Получает число от пользователя с проверкой ввода"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Ошибка: Введите корректное число!")

def main():
    """Главная функция калькулятора"""
    calc = Calculator()
    
    print("🧮 ДОБРО ПОЖАЛОВАТЬ В КОНСОЛЬНЫЙ КАЛЬКУЛЯТОР!")
    print("=" * 50)
    
    while True:
        display_menu()
        
        try:
            choice = input("Выберите операцию (1-6): ").strip()
            
            if choice == '6':
                print("\n👋 До свидания! Спасибо за использование калькулятора!")
                break
            
            elif choice == '5':
                calc.show_history()
                continue
            
            elif choice in ['1', '2', '3', '4']:
                print("\n--- Введите числа для вычисления ---")
                num1 = get_number("Введите первое число: ")
                num2 = get_number("Введите второе число: ")
                
                try:
                    if choice == '1':
                        result = calc.add(num1, num2)
                        operation = "+"
                    elif choice == '2':
                        result = calc.subtract(num1, num2)
                        operation = "-"
                    elif choice == '3':
                        result = calc.multiply(num1, num2)
                        operation = "×"
                    elif choice == '4':
                        result = calc.divide(num1, num2)
                        operation = "÷"
                    
                    print(f"\n✅ РЕЗУЛЬТАТ: {num1} {operation} {num2} = {result}")
                    
                except ValueError as e:
                    print(f"❌ {e}")
                
            else:
                print("❌ Ошибка: Выберите операцию от 1 до 6!")
                
        except KeyboardInterrupt:
            print("\n\n👋 Программа прервана пользователем. До свидания!")
            break
        except Exception as e:
            print(f"❌ Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()