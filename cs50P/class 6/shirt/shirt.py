import sys
import os
from PIL import Image, ImageOps

def main():
    images()


def images():
    extensions = [".jpg", ".png", ".jpeg"]
    extsin = []
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        files = [sys.argv[1], sys.argv[2]]
        for file_path in files:
            root, ext = os.path.splitext(file_path)
            if ext in extensions:
                extsin.append(ext)
            else:
                sys.exit("wrong file extension")
        if extsin[0] != extsin[1]:
            sys.exit("file extensions are not the same")
        before = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        before = ImageOps.fit(before, shirt.size)
        before.paste(shirt, (0,0), shirt)
        before.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("no such file exists")

if __name__ == "__main__":
    main()
