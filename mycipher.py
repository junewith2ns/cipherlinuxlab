import sys

cipherTxt = ""
charCounter = 0
lineCounter = 0

rotation = int(sys.argv[1])

plainTxt = sys.stdin.read()

for character in plainTxt:
    if character.isalpha():
        character = character.upper()
        shiftedChar = chr((ord(character) - 65 + rotation) % 26 + 65)
        cipherTxt += shiftedChar
        charCounter += 1
        lineCounter += 1

        if charCounter == 5:
            cipherTxt += " "
            charCounter = 0

        if lineCounter == 50:
            cipherTxt += "\n"
            lineCounter = 0

print(cipherTxt)