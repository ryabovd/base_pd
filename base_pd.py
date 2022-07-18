import csv
from datetime import date
import sys
import ctypes
import pprint


kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

'''
Colors!
Write a module and import in future.
'''
red_text = '\033[31m'
green_text = '\033[32m'
yellow_text = '\033[33m'
blue_text = '\033[34m'
white_text_on_blue = '\033[37m\033[44m'
marked_text = '\033[43m'
end_text = '\033[0m'
numbers = white_text_on_blue


def main():
    '''
    Main function.
    Base structure.
    '''
    base_file = "base_pd.csv"
    base_structure = [
        'Фамилия Имя Отчество (с учетом РЕГИСТРА)', 
        'Дата рождения dd.mm.yyyy', 
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
    '''
    Menu function
    '''
    menu_choise = 'выбор не сделан'
    print("\033[4m{}\033[0m".format("\nМЕНЮ"))
    print(numbers + " " + "1" + " " + end_text + " - Найти запись")
    print(numbers + " " + "2" + " " + end_text + " - Внести записи")
    print(numbers + " " + "3" + " " + end_text + " - Изменить запись")
    print(numbers + " " + "4" + " " + end_text + " - Напечатать все записи")
    print(numbers + " " + "0" + " " + end_text + " - Выход \n")
    menu_choise = input("Выберите " + numbers + "пункт" + end_text + " меню - " + blue_text).strip()
    print(end_text, end='')
    while menu_choise not in ['0', '1', '2', '3', '4']:
        menu_choise = input(red_text + "Неправильный выбор\n" + end_text + "Выберите " + numbers + "пункт" + end_text + " меню - " + blue_text).strip()
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
        print(green_text + "ВЫХОД из программы" + end_text)
        sys.exit()
    else:
        pass


def rec_find(base_file):
    '''Func that recieved basefile name and printed list of finded records'''
    record = input("Введите ФИО для поиска: (с учетом РЕГИСТРА) ").strip()
    base_list = base_file_read(base_file)
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
        print()
        print(numbers + ' № ' + end_text + '     Запись' + '\n')
        for rec in range(len(find_list)):
            print(numbers + ' ' + str(find_list[rec][0]) + ' ' + end_text, ' ', end='')
            pprint.pprint(find_list[rec][1], indent=4, width=200)
            print()
    else:
        print('\nЗапись', marked_text + record + end_text, red_text + 'НЕ НАЙДЕНА' + end_text)
        print(green_text + 'Работа программы ЗАВЕРШЕНА' + end_text)
        sys.exit()


def rec_new(base_file, base_structure):
    '''Make error handling of non-numerical inputs
    Make input handling 0'''
    n = int(input("Введите количество записей для ввода - ").strip())
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
        print(green_text + "Внесена запись" + end_text)
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
    rec_for_change = input('Введите ' + numbers + ' № ' + end_text + ' записи для изменения - ' + blue_text).strip()
    print(end_text, end='')
    for rec in find_list:
        if rec_for_change == str(rec[0]):
            print(red_text + 'Изменить запись???' + end_text, yellow_text + str(rec) + end_text)
            choise = input('Напишите ' + red_text + 'ДА' + end_text + ' или ' + green_text + 'НЕТ' + end_text + ' - ').strip()
            if choise.lower() == 'да':
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
        print("ПРОВЕРЬТЕ данные: " + base_structure[y])
        print(new_record[y])
        print()
        choise = input("Изменить данные? Введите " + red_text + "ДА" + end_text + " или " + green_text + "НЕТ" + end_text + " - ").strip()
        if choise.lower() == 'да':
            new_data = input('Введите данные: '+ base_structure[y] + ' - ').strip()
            new_record[y] = new_data
        else:
            continue
    if new_record[-1] != date_today():
        date = date_today()    
        new_record[-1] = date
        print(red_text + 'Запись ИЗМЕНЕНА' + end_text, date)
    record_for_write = (record_for_change[0], new_record)
    base_list = preper_base_list(base_list, record_for_write)
    write_change_base_file(base_file, base_list)


def preper_base_list(base_list, record_for_write):
    '''Insert a new record in place of the old one'''
    index, line = record_for_write
    base_list[index] = line
    return base_list


def write_change_base_file(base_file, base_list):
    '''Func recieved name base file and new base list. 
    Then write base file from list.'''
    with open(file=base_file, mode="w", encoding="UTF-8", newline='') as base:
        writer = csv.writer(base, delimiter=';')
        for line in base_list:
            writer.writerow(line)
    print(red_text + "Файл базы данных ЗАПИСАН" + end_text + "\n")


if __name__ == "__main__":
    main()
    print(green_text + 'Работа программы ЗАВЕРШЕНА' + end_text)
