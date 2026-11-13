import random
def run():
    return random.randint(1,11)
names=['borg','wolf','theaf','goblin','knight']
def enemy(name):
    return random.choice(name)
def enemdmg():
    return random.randint(1,15)
def enemhp():
    return random.randint(25,90)
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
    print(f"health points: {hpp} (+20 hp per health stat)")
    print(f"dexarity points: {dexp} (+1/10 chance to dodge per dex stat)")
strth=strp*5
hp=hpp*5
dextar=dexp*5

while True:
    nameem=enemy
    enehp=enemhp
    enedmg=enemdmg
    print(f"you are being attacked by a {nameem} with {enehp} health points and dose {enedmg} damage to you")
    attack=input("do you want to attack(1) heal(2) flee(3)")
    if attack == "1":
        enehp -= strth
        if enehp <= 0:
            print(f"you killed the {nameem}")
            break
        else:
            print("enemy turn"):
    if attack == "2":
        hp += 5
    if attack == "3":
        please=input("chose how you run 1-10")
        if please == run:  
            print("you sucsessfuly ran for your life")
            break
        else:
            print(f"you didnt excape the{nameem}")