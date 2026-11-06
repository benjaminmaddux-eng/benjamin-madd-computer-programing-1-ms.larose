#benjmain maddux cyper code ms.larose
def code(mesage, shift):
    '''this orders the alhpa bet and checks if its uper case then adds the shift to the count of 26 becuse there are 26 letters in the alphabet i also used % insted of / becuse google sayed to do that and it worked and it turns out its modulo to make it loop to A if its Z '''
    thing = ""
    for char in mesage:
        if char.isalpha():
            if char.isupper():
                thing += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                thing += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            thing += char
    return thing
def dcode(mesage, shift):
    '''this just inverses the funtion: code'''
    return code(mesage, -shift)
dih = input("Choose (1 for encode, 2 for decode): ")
mesage = input("input: ")
shift = int(input("input the shift: "))#choses how far it shifts in the alphbte
if dih == "1":
    result = code(mesage, shift)
    print("coded mesage:", result)
elif dih == "2":
    result = dcode(mesage, shift)
    print("Dcoded mesage:", result)
else:
    print("choose 1 or 2.")
#idk how to make this work with numbers i might just add +1 per shift 