import sys
import csv


def main():
    print(text())


def text():
    data=[]
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
            sys.exit("no .csv file")
        else:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last, first = row["name"].split(", ")
                    data.append({"first": first, "last": last, "house": row["house"]})
            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for _ in data:
                    writer.writerow(_)
    except FileNotFoundError:
        sys.exit("no such file exists")

if __name__ == "__main__":
    main()
