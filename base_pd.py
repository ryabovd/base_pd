import csv


def main():
    base_file = "base_pd.csv"
    base_structure = ['ФИО', 'Дата рождения yyyy.mm.dd', 'Место рождения', 'Паспорт (Номер, Кем выдан, Дата выдачи, Код подразделения)', 'СНИЛС', 'ИНН']
    #print(base_file_read(base_file))
    menu_choise = menu()
    menu_handling(menu_choise, base_file, base_structure)

"""
   base_file_read(base_file)
    
    n = int(input("Введите количество записей для ввода "))
    data_list = []
    for i in range(n):
        data = []
        for y in range(len(base_structure)):
            data_input = input("Введите данные: " + base_structure[y] + " ")
            data.append(data_input)
        base_file_write(base_file, data)
"""

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
        menu_choise = input("Неправильный выбор\nВыберите пункт меню - ")
    print('Выбор', menu_choise)
    return menu_choise

def menu_handling(menu_choise, base_file, base_structure):
    if menu_choise == '1':
        rec_find(base_file)
    if menu_choise == '2':
        rec_new(base_file, base_structure)

def rec_find(base_file):
    record = input("Введите ФИО для поиска: ")
    base_list =  base_file_read(base_file)
    #print(reader)
    for rec in base_list:
        if record in rec[0]:
            print(rec)
        elif rec == []:
            continue
        else:
            continue
    print("Что дальше?")

def rec_new(base_file, base_structure):
    n = int(input("Введите количество записей для ввода "))
    data_list = []
    for i in range(n):
        data = []
        for y in range(len(base_structure)):
            data_input = input("Введите данные: " + base_structure[y] + " ")
            data.append(data_input)
            print(data)
        base_file_write(base_file, data)
    
def base_file_read(base_file):
    with open(file=base_file, mode="r", encoding="UTF-8") as base:
        reader = csv.reader(base, delimiter = ';')
        base_list = []
        for row in reader:
            #print(row)
            base_list.append(row)
        return(base_list)


def base_file_write(base_file, data):
    print(data)
    with open(file=base_file, mode="a", encoding="UTF-8", newline='') as base:
        writer = csv.writer(base, delimiter=';')
        writer.writerow(data)

if __name__ == "__main__":
    main()