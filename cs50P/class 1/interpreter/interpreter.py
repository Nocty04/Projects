def main():
    calculation = input(" ")
    x, y, z = calculation.split(" ")
    if y == "+":
        result = int(x) + int(z)
    elif y == "-":
        result = int(x) - int(z)
    elif y == "*":
        result = int(x) * int(z)
    elif y == "/":
        result = int(x) / int(z)
    print(f"{result:.1f}")

main()
