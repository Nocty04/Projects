import sys

def main():
    print(line_count())


def line_count():
    n = 0
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".py"):
            sys.exit("no .py file")
        else:
            with open(sys.argv[1]) as file:
                for line in file:
                    data = line.strip()
                    if data == "" or data.startswith("#"):
                        pass
                    else:
                        n += 1
                return n
    except FileNotFoundError:
        sys.exit("no such file exists")

if __name__ == "__main__":
    main()




