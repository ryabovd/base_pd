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
        'Телефон (+7********** несколько через запятую)', 
        'e-mail (несколько через запятую)', 
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
        change_data(base_file, base_structure)
    elif menu_choise == '4':
        print_all_data(base_file)
    elif menu_choise == '0':
        print("ВЫХОД из программы")
        sys.exit()
    else:
        pass

def rec_find(base_file):
    '''Func that recieved basefile name and printed list of finded records'''
    record = input("Введите ФИО для поиска: ")
    base_list =  base_file_read(base_file)
    find_list = get_find_list(base_list, record)
    print_find_list(find_list, record)
    return find_list
            
def get_find_list(base_list, record):
    '''Func recieved list of records and returned list of finded records and theyes indexes'''
    find_list = []
    for rec in range(len(base_list)):
        if record in base_list[rec][0]:
            finded_record = rec, base_list[rec]
            find_list.append(finded_record)
        elif base_list[rec] == []:
            continue
        else:
            continue
    return find_list

def print_find_list(find_list, record):
    '''Func recieved list of finded records and record that need to find.
    Printed heads.
    For rec in base printed index of finded record and finded record.
    if record not in base, print notice.
    '''
    if len(find_list) > 0:
        print('\n№     Запись')
        for rec in range(len(find_list)):
            print(find_list[rec][0], ' ', find_list[rec][1])
    else:
        print('\nЗапись', record, 'НЕ НАЙДЕНА')
    print("\nЧто дальше?")

def rec_new(base_file, base_structure):
    '''Сделать обработку ошибки ввода не числа
    Сделать обработку ввода 0'''
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
    '''Func that reads csv file (delimiter is ';') and returns a list of lists of strings'''
    with open(file=base_file, mode='r', encoding='utf-8') as base:
        lines = csv.reader(base, delimiter=';')
        base_list = list(lines)
    return base_list

def base_file_write(base_file, data):
    with open(file=base_file, mode="a", encoding="UTF-8", newline='') as base:
        writer = csv.writer(base, delimiter=';')
        writer.writerow(data)
        print("Внесена запись")
        print(data)

def print_all_data(base_file):
    '''Func print all data from basefile'''
    base = base_file_read(base_file)
    for rec in base:
        print(( ';').join(rec) + '\n')

def change_data(base_file, base_structure):
    '''Func finds records on request.
    '''
    find_list = rec_find(base_file)
    rec_for_change = input('Введите номер записи для изменения - ').strip()
    for rec in find_list:
        if rec_for_change == str(rec[0]):
            print('Изменить запись???', rec)
            choise = input('Напишите "да" или "нет" - ').strip()
            if choise == 'да':
                base_list = base_file_read(base_file)
                change_record(rec, base_structure, base_list, base_file)
            else:
                print('Не меняем записи')
        else:
            continue

def change_record(record_for_change, base_structure, base_list, base_file):
    '''Func recieve tuple.
    Save position 0 in new record.
    And check all data in position 1'''
    print(record_for_change)
    new_record = record_for_change[1]
    if len(new_record) < len(base_structure):
        for n in range(len(base_structure) - len(new_record)):
            new_record.append(' ')
    for y in range(len(base_structure) - 1):
        print("Проверьте данные: " + base_structure[y])
        print(new_record[y])
        print()
        choise = input('Изменить данные? Введите "да" или "нет" - ').strip()
        if choise.lower() == 'да':
            new_data = input('Введите данные: '+ base_structure[y] + ' - ').strip()
            new_record[y] = new_data
        else:
            continue
    if new_record[-1] != date_today():
        date = date_today()    
        new_record[-1] = date
        print('Изменена дата редактирования записи - ', date)
    record_for_write = (record_for_change[0], new_record)
    base_list = preper_base_list(base_list, record_for_write)
    write_change_base_file(base_file, base_list)

def preper_base_list(base_list, record_for_write):
    index, line = record_for_write
    base_list[index] = line
    return base_list

def write_change_base_file(base_file, base_list):
    '''Func recieved name base file and new base list. 
    Then write base file from list.'''
    with open(file=base_file, mode="w", encoding="UTF-8", newline='') as base:
        writer = csv.writer(base, delimiter=';')
        for line in base_list:
            #print(line)
            writer.writerow(line)
    print("Файл базы данных записан")


if __name__ == "__main__":
    main()