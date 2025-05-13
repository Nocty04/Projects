import inflect
p = inflect.engine()

def main():
    Liste = []


    while True:
        try:
            name = input("name: ")
            Liste.append(name)
        except EOFError:
            break
    a = p.join(Liste)
    print(f"Adieu, adieu, to {a}")


main()
