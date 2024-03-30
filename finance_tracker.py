import json
import os

def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return {'income': [], 'expenses': []}

def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)

def add_transaction(data):
    while True:
        try:
            amount = float(input("Введите сумму: "))
            break
        except ValueError:
            print("Ошибка: Введите корректное число для суммы.")

    description = input("Введите описание: ")
    
    while True:
        category = input("Введите категорию (доход/расход): ").lower()
        if category in ['доход', 'расход']:
            break
        else:
            print("Ошибка: Введите 'доход' или 'расход'.")

    if category == 'доход':
        data['income'].append({'amount': amount, 'description': description})
    elif category == 'расход':
        data['expenses'].append({'amount': amount, 'description': description})

def delete_transaction(data):
    category = input("Введите категорию для удаления (доход/расход): ").lower()
    if category == 'доход':
        if data['income']:
            print("Выберите номер записи для удаления:")
            for i, income in enumerate(data['income']):
                print(f"{i+1}. Сумма: {income['amount']}, Описание: {income['description']}")
            try:
                index = int(input("Введите номер записи: ")) - 1
                del data['income'][index]
                print("Запись успешно удалена.")
            except (IndexError, ValueError):
                print("Ошибка: Введите корректный номер записи.")
        else:
            print("Нет доступных записей для удаления.")
    elif category == 'расход':
        if data['expenses']:
            print("Выберите номер записи для удаления:")
            for i, expense in enumerate(data['expenses']):
                print(f"{i+1}. Сумма: {expense['amount']}, Описание: {expense['description']}")
            try:
                index = int(input("Введите номер записи: ")) - 1
                del data['expenses'][index]
                print("Запись успешно удалена.")
            except (IndexError, ValueError):
                print("Ошибка: Введите корректный номер записи.")
        else:
            print("Нет доступных записей для удаления.")
    else:
        print("Некорректная категория.")

def show_report(data):
    print("Отчет по доходам:")
    for income in data['income']:
        print(f"Сумма: {income['amount']}, Описание: {income['description']}")
    
    print("\nОтчет по расходам:")
    for expense in data['expenses']:
        print(f"Сумма: {expense['amount']}, Описание: {expense['description']}")

def main():
    file_name = 'finance_data.json'
    data = load_data(file_name)
    
    while True:
        print("\n1. Ввод данных")
        print("2. Отчет")
        print("3. Удаление записи")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_transaction(data)
            save_data(data, file_name)
        elif choice == '2':
            show_report(data)
        elif choice == '3':
            delete_transaction(data)
            save_data(data, file_name)
        elif choice == '4':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()
