import random

def main():
    generate_integer(get_level())

def get_level():
    while True:
        try:
            level = input("level: ")
            level = int(level)
            if level in [1,2,3]:
                return level
            else:
                pass
        except ValueError:
            pass

def generate_integer(x):
  #gerar dois numeros de acordo com o nivel
    z = True
    score = 0
    for _ in range(10):
        if x == 1:
            a = random.randint(0, 9)
            b = random.randint(0, 9)
        elif x == 2:
            a = random.randint(10, 99)
            b = random.randint(10, 99)
        else:
            a = random.randint(100, 999)
            b = random.randint(100, 999)
        for _ in range(3):
            c = a + b
            calc = input(f"{a} + {b} = ")
            try:
                if int(calc) == c:
                    z = True
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                z = False
                print("EEE")
        if z == False:
            print(f"{a} + {b} = {c}")
            score = score
    print(score)


if __name__ == "__main__":
    main()
