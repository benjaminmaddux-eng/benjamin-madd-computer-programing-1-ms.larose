import random
names=['borg','wolf','theaf','goblin','knight']
def enemy(name):
    return random.choice(name)

strp=0
hpp=0
dexp=0
upp=10
while True:
    thing=input(f"please input your stats, you have [{upp}] points left for upgrades 1 is for strength +1 2 is for health +1 and 3 is for dextarity: ")
    if thing == "1":
        upp -= 1
        strp += 1
    if thing == "2":
        upp-=1
        hpp += 1
    if thing == "3":
        upp-=1
        dexp += 1
    if upp == 0:
        print(" you are out of upgrade points")
        break
    print(f"strenght points: {strp} (+5 dmg per strenght stat)")
    print(f"health points: {hpp} (+20 hp per strenght stat)")
    print(f"dexarity points: {dexp} (+1/10 chance to dodge per strenght stat)")
