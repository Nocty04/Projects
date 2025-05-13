def main():
    x = input("say a greeting. ")
    x = x.lower().strip()
    if x.startswith("hello"):
        print("$0")
    elif x.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
