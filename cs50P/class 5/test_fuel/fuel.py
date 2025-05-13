def main():
    perc = input("Fraction: ")
    x = convert(perc)
    print(gauge(x))

def convert(fraction):
    while True:
        n = fraction.split("/")
        try:
            fraction = int(n[0]) / int(n[1]) * 100
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError
        else:
            if fraction <= 100:
                return (round(fraction))
            else:
                raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return ("E")
    elif percentage >= 99:
        return ("F")
    else:
        a = str(percentage) + "%"
        return a

if __name__ == "__main__":
    main()
