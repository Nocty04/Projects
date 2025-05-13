import re

def main():
    print(validate(input("ipv4 adress: ")))

def validate(ip):
    n = r"([0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
    if ip := re.search(fr"^{n}\.{n}\.{n}\.{n}$", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
