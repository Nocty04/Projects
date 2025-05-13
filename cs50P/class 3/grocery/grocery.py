def main():
    grocery()


def grocery():


    List = {}
    while True:
        try:
            food = input("").upper()
        except EOFError:
            for food in sorted(List):
                print(f"{List[food]} {food}")
            break
        else:
            if food in List:
                List[food] += 1
            else:
                List[food] = 1



main()
