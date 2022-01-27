import csv


def main():
    base_file = "base_pd.csv"
    base_file_read(base_file)

def base_file_read(base_file):
    with open(file=base_file, mode="r", encoding="UTF-8") as base:
        reader = csv.reader(base, delimiter = ';')
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()