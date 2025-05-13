import random
import sys

def main():
        while True:
            level = input("level: ")
            try:
                if int(level) > 0:
                    n = random.randint(1, int(level))
                    break
                else:
                    pass
            except ValueError:
                print("invalid")
        while True:
            guess = input("guess: ")
            try:
                guess = int(guess)
                if guess < n:
                    print("Too small!")
                elif guess > n:
                    print("Too large!")
                else:
                    sys.exit("Just right!")
            except ValueError:
                print("invalid")





main()
