#benjmain maddux cyper code ms.larose
import pandas as pd
thing=list(input("input your password:").lower())
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for thing in letters:
    pyfer=thing.shift(letters,1)