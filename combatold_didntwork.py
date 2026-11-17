import random



names=["borg","wolf","theaf","goblin","knight"]

nameem=random.choice(names)

enemdmg=random.randint(1,15)

enemhp=random.randint(25,90)

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
    print(f"dexarity points: {dexp} (+1/10 chance to dodge per dex stat) and added chance to flee from a fight")
strth=int(strp*5)
raning=dexp+2
def run():
    random.randint(1,raning)

hp=hpp*5

dextar=int(dexp*5)  
enehp=enemhp
enedmg=enemdmg
print(f"you are being attacked by a {nameem} with {enehp} health points and dose {enedmg} damage to you")
while True:
    print(f"you have: {hp} health")
    print(f"the {nameem} has: {enehp} health")
    attack=input("do you want to attack(1) heal(2) flee(3)")
    if attack == "1":
        enehp -= int(strth)
        if enehp <= 0:
            print(f"you killed the {nameem}")
            break
        else:
            print("enemy turn")
            if run() == 1:
                hp -= enemdmg
                if hp <= 0:
                    print("you have been defeated")
                    break
            else:
                print("you dodged the attack")
    if attack == "2":
        hp += 5
    if attack == "3":
        if run() != 1:
            print("you sucsessfuly ran for your life")
            break
        else:
            print(f"you didnt escape the{nameem}")