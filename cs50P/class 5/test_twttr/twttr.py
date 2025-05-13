def main():
    x = input("enter a text: ")
    print(shorten(x))

def shorten(letra):
    result = ""
    for i in range(len(letra)):
     if letra[i] in ["a","i","e","o","O","I","U"]:
      result += ""
     else:
      result += letra[i]
    return result


if __name__ == "__main__":
    main()
