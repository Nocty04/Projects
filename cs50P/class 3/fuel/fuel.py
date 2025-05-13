def main():
    x = transform()
    print(reading(x))

def transform():
    while True:
        perc = input("Fraction: ")
        n = perc.split("/")
        try:
            fraction = int(n[0]) / int(n[1]) * 100
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if fraction <= 100:
                return (round(fraction))
            else:
                pass

def reading(n):
    if n <= 1:
        return ("E")
    elif n >= 99:
        return ("F")
    else:
        a = str(n) + "%"
        return a

main()
