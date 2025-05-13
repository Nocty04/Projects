import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
        if s := re.search(r"^([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([0-9]|[1][0-2]):?([0-5][0-9])? (AM|PM)$",s):
            if s.group(2) == None and s.group(5) == None:
                minute_begin,  minute_final = "00", "00"
            elif s.group(2) == None:
                minute_begin,  minute_final = "00", s.group(5)
            elif s.group(5) == None:
                minute_begin, minute_final = s.group(2), "00"
            else:
                minute_begin, minute_final = s.group(2), s.group(5)
            if (s.group(1) == "12" and minute_begin != "00") or (s.group(4) == "12" and minute_final != "00"):
                raise ValueError
            if s.group(3) == "AM" and s.group(6) == "PM":
                if s.group(1) != "12" or s.group(4) != "12":
                    hour_begin = f"{int(s.group(1)):02}:{minute_begin}"
                    hour_final = f"{(int(s.group(4)) + 12):02}:{minute_final}"
                elif s.group(1) == "12" and s.group(4) != "12":
                    hour_begin = f"00:{minute_begin}"
                elif s.group(1) != "12" and s.group(4) == "12":
                    hour_final = f"12:{minute_final}"
                else:
                    hour_begin = f"00:{minute_begin}"
                    hour_final = f"12:{minute_final}"
            elif s.group(3) == "PM" and s.group(6) == "AM":
                if s.group(1) != "12" and s.group(4) != "12":
                    hour_begin = f"{(int(s.group(1)) + 12):02}:{minute_begin}"
                    hour_final = f"{int(s.group(4)):02}:{minute_final}"
                elif s.group(1) == "12" and s.group(4) != "12":
                    hour_begin = f"12:{minute_begin}"
                elif s.group(1) != "12" and s.group(4) == "12":
                    hour_final = f"00:{minute_final}"
                else:
                    hour_begin = f"12:{minute_begin}"
                    hour_final = f"00:{minute_final}"
            else:
                raise ValueError
            result= f"{hour_begin} to {hour_final}"
            return result
        else:
            raise ValueError



if __name__ == "__main__":
    main()
