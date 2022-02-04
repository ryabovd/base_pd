import csv
from datetime import date
import sys


def main():
    base_file = "base_pd.csv"
    base_structure = [
        'Фамилия Имя Отчество', 
        'Дата рождения yyyy.mm.dd', 
        'Место рождения', 
        'Паспорт (Номер, Кем выдан, Дата выдачи, Код подразделения)', 
        'СНИЛС (только цифры)', 
        'ИНН', 
        'Адрес (Индекс, Регион, Город, Улица, Дом, Квартира)', 
        'Телефон (+7**********)', 
        'e-mail', 
        'Дата актуальности'
        ]
    menu_choise = menu()
    menu_handling(menu_choise, base_file, base_structure)

def menu():
    menu_choise = 'выбор не сделан'
    print("МЕНЮ")
    print("1 - Найти запись")
    print("2 - Внести записи")
    print("3 - Изменить запись")
    print("4 - Напечатать все записи")
    print("0 - Выход")
    print()
    menu_choise = input("Выберите пункт меню - ")
    while menu_choise not in ['0', '1', '2', '3', '4']:
        menu_choise = input("Неправильный выбор\nВыберите пункт меню - ").strip()
    print('Выбор', menu_choise)
    return menu_choise

def menu_handling(menu_choise, base_file, base_structure):
    if menu_choise == '1':
        rec_find(base_file)
    elif menu_choise == '2':
        rec_new(base_file, base_structure)
    elif menu_choise == '3':
        pass
    elif menu_choise == '4':
        print_all_data(base_file)
    elif menu_choise == '0':
        print("ВЫХОД из программы")
        sys.exit()
    else:
        pass

def rec_find(base_file):
    record = input("Введите ФИО для поиска: ")
    base_list =  base_file_read(base_file)
    find_list = get_find_list(base_list, record)
    print_find_list(find_list, record)
            
def get_find_list(base_list, record):
    find_list = []
    for rec in base_list:
        if record in rec[0]:
            find_list.append(rec)
        elif rec == []:
            continue
        else:
            continue
    return find_list

def print_find_list(find_list, record):
    if len(find_list) > 0:
        print('\n№   Запись')
        for rec in range(len(find_list)):
            print(rec + 1, ' ', ('; ').join(find_list[rec]))
    else:
        print('\nЗапись', record, 'НЕ НАЙДЕНА')
    print("\nЧто дальше?")

def rec_new(base_file, base_structure):
    n = int(input("Введите количество записей для ввода - "))
    data_list = []
    for i in range(n):
        data = []
        for y in range(len(base_structure) - 1):
            data_input = input("Введите данные: " + base_structure[y] + " - ").strip()
            if y == 0:
                if check_name(data_input, base_file) is True:
                    print("Такая запись уже внесена.\nОСТАНОВКА программы\n")
                    break
                else:
                    data.append(data_input)
            else:
                data.append(data_input)
        if len(data) > 1:
            date = date_today()
            data.append(date)
            base_file_write(base_file, data)

def check_name(data_input, base_file):
    record = False
    data = base_file_read(base_file)
    for rec in data:
        if rec[0] == data_input:
            record = True
            return record
        else:
            continue
    return record

def date_today():
    '''Func that returned today date'''
    today = date.today()
    return today
    
def base_file_read(base_file):
    with open(file=base_file, mode="r", encoding="UTF-8") as base:
        reader = csv.reader(base, delimiter = ';')
        base_list = []
        for row in reader:
            base_list.append(row)
        return(base_list)

def base_file_write(base_file, data):
    with open(file=base_file, mode="a", encoding="UTF-8", newline='') as base:
        writer = csv.writer(base, delimiter=';')
        writer.writerow(data)
        print("Внесена запись")
        print(data)
        #menu()

def print_all_data(base_file):
    base = base_file_read(base_file)
    for rec in base:
        print(( ';').join(rec))


if __name__ == "__main__":
    main()