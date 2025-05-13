def main():
    x = input("what time is it? ")
    meal_time = convert(x)
    if 7 <= meal_time <= 8:
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")
    else:
        print("")

def convert(time):
    time = time.split(":")
    minute = float(time[1])
    hour = float(time[0])
    final_time = hour + minute / 60
    return final_time



if __name__ == "__main__":
    main()
