import sys
from tabulate import tabulate
import csv

def main():
    print(pizza())

def pizza():
    pizzas = []
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("no .csv file")
        else:
            with open(sys.argv[1]) as file:
                type = sys.argv[1].replace(".csv", "")
                type_pizza = f"{type.title()} Pizza"
                reader = csv.DictReader(file)
                for row in reader:
                    pizzas.append({type_pizza: row[type_pizza], "Small": row["Small"], "Large": row["Large"]})
                print(tabulate(pizzas, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("no such file exists")


if __name__ == "__main__":
    main()
