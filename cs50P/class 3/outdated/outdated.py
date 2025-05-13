def main():
    date()

months   =  ["January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]


data = {month: index + 1 for index, month in enumerate(months)}

def date():
    List = []
#loop ate ser valido
    while True:
        try:
            a = input("Date: ").capitalize()
            if "/" in a:
                List = a.strip().split("/")
#to try and grab if the user inputs month/int/int
                try:
                    if int(List[0]):
                        b = True
                except ValueError:
                        b = False

            elif "," in a:
                List = a.strip().replace(",", "").split(" ")
#to try to check if the user inputs the month in wrong place for example 9 october,
                if List[0] not in data:
                    b = False
                else:
                    b = True
            else:
                b = False
# verifica se o que o user inseriu foi o mes ou o numero do dicionario
            if b:
                if len(List) == 3:
                    if 1 <= int(List[1]) <= 31:
                        try:
                            if 1 <= int(List[0]) <= 12 :
                                print(f"{List[2]}-{int(List[0]):02d}-{int(List[1]):02d}")
                                break
                            else:
                                print("Invalid")
                        except ValueError:
                            if List[0] in data:
                                month_numb = data[List[0]]
                                day_part = int(List[1])
                                print(f"{List[2]}-{month_numb:02d}-{day_part:02d}")
                                break
                            else:
                                print("Invalid")
                    else:
                        print("Invalid")
                else:
                    print("Invalid")
        except EOFError:
            return




main()

