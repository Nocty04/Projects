import re



def main():
    print(count(input("Text: ")))


def count(s):
    n = f" {s} "
    if n := re.findall(r"(\W|\s)um(\W|\s)",n, re.IGNORECASE):
        if len(n) == None:
            return 0
        else:
            return len(n)

if __name__ == "__main__":
    main()
