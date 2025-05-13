from datetime import date
import re
import sys
import inflect


class Date:
    def __init__(self, date_s):
        if date_s := re.search(r"([0-9]{4})-(1[0-2]|0[1-9])-(0[1-9]|[1-2][0-9]|3[0-1])", date_s):
            self.year = int(date_s.group(1))
            self.month = int(date_s.group(2))
            self.day = int(date_s.group(3))
            self.d = date(self.year, self.month, self.day)
        else:
            sys.exit("invalid date")

    def __sub__(self, other):
        if isinstance(other, Date):
            self.result = self.d - other.d
            self.minutes = self.result.days * 24 * 60
            return self
        else:
            raise ValueError

    def __str__(self):
        p = inflect.engine()
        return p.number_to_words(self.minutes, andword="")

def main():
    dob = Date(input("Date of birth: "))
    today = Date(str(date.today()))
    final = str(today - dob).capitalize()
    print(f"{final} minutes")


if __name__ == "__main__":
    main()
