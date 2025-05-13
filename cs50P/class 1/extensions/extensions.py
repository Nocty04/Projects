def main():
    name = input("insert file name ")
#manipula a string para que fica minuscula tire espaços e separe o .--- do resto
    name = name.lower().strip()
    n = name.rsplit(".", maxsplit=1)
    file = n[1]
    find_file(file)

def find_file(x):
    match x:
        case "gif":
            print("image/gif")
        case "jpg"|"jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


main()



