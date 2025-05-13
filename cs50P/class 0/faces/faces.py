def main():
 x = input("")
 print(convert(x))

def convert(emotion):
 emotion = emotion.replace(":)","🙂")
 emotion = emotion.replace(":(","🙁")
 return emotion

main()

