import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if not "iframe" in s:
        return None
    elif s := re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w{11})",s):
        result = f" https://youtu.be/{s.group(1)}"
        return result
    else:
        return None





if __name__ == "__main__":
    main()
