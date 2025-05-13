from validator_collection import validators

def main():
    print(is_valid(input("Email: ")))

def is_valid(e):
    try:
        e = validators.email(e)
        return "Valid"
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()

