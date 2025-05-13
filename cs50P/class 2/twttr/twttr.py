def main():
    x = input("enter a text: ")
    print(convert(x))

def convert(letra):
    result = " "
    for i in range(len(letra)):
     if letra[i] in ["a","i","u","e","o","O","E","I","A","U"]:
      result += ""
     else:
      result += letra[i]
    return result


if __name__ == "__main__":
    main()
