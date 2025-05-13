def main():
    menu()


def menu():
    x = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }
    a = 0.00
    while True:
        try:
            food = input(" ").title()
        except EOFError:
            break
        try:
            a += float(x[food])
            b = (f"Total: ${a:.2f}")
            print (b)
        except KeyError:
            pass
        except ValueError:
            pass






main()
