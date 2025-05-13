def main():
    camel = input("Enter a name of a variable in camel case ")
    print(transform(camel))


#checka por upper cases se true grava a posição busca a lista da outra
def transform(x):
   convert(x)
   result = ""
   for i in range(len(x)):
      if x[i].isupper() and i != 0:
          result += "_" + x[i].lower()
      else:
          result += x[i].lower()
   return result

#transforma isto numa lista

def convert(string):
     s = " ".join(string)
     letters = s.split()
     return letters

main()

