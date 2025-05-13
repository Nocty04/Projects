def main():
    coke()


def coke():
    x = 50
    print("Amount Due:", x)
    while x > 0:
       coin = input("Insert coin: ")
       change = int(coin)
       if change in [5,10,25]:
          x = x - change
          if x > 0:
            print("Amount Due:", x)
          else:
            print ("Change Owed:", -x)
       else:
           print("Amount Due:", x)

main()


