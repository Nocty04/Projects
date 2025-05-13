import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    Lista = figlet.getFonts()

    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("invalid usage")
        sys.exit(1)
    elif len(sys.argv) == 3:
        fonte = sys.argv[2]
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print("invalid Usage")
            sys.exit(1)
        elif fonte not in Lista:
            print("invalid Usage")
            sys.exit(1)
        else:
            figlet.setFont(font = fonte)
    else:
        f = random.choice(Lista)
        figlet.setFont(font = f)


    text = input("Text: ")
    print(figlet.renderText(text))


main()

