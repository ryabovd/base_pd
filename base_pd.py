import csv


def main():
    base_file = "base_pd.csv"
    base_structure = ['ФИО', 'Дата рождения yyyy.mm.dd', 'Место рождения', 'Паспорт (Номер, Кем выдан, Дата выдачи, Код подразделения)', 'СНИЛС', 'ИНН']
    base_file_read(base_file)
    
    n = int(input("Введите количество записей для ввода "))
    data_list = []
    for i in range(n):
        data = []
        for y in range(len(base_structure)):
            data_input = input("Введите данные: " + base_structure[y] + " ")
            data.append(data_input)
        base_file_write(base_file, data)

def base_file_read(base_file):
    with open(file=base_file, mode="r", encoding="UTF-8") as base:
        reader = csv.reader(base, delimiter = ';')
        for row in reader:
            print(row)

def base_file_write(base_file, data):
    print(data)
    with open(file=base_file, mode="a", encoding="UTF-8") as base:
        writer = csv.writer(base, delimiter=';')
        writer.writerow(data)

if __name__ == "__main__":
    main()