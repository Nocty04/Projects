def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 > len(s) or len(s) > 6:
        return False
    if not s.isalnum():
        return False
    if not s[0:2].isalpha():
        return False
#verifica se o primeiro digito é zero
    isFirst = True
    for n in range(len(s)):
         if s[n].isdigit():
            if isFirst:
                 isFirst = False
                 if s[n] == "0":
                     return False
#verifica se ha alguma posiçao de alfabeto numa posiçao a frente do numero
    number = False
    for n in range(len(s)):
        if s[n].isdigit():
            number = True
        elif number and s[n].isalpha():
            return False

    return True









main()
