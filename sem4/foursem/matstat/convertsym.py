text = str()


while True:
    try:
        i = input()
    except EOFError:
        break
    text += (i.replace(',', '.')) + " "

print (text)