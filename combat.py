# benmaddux comouter programing mslarose

import random

names = ["borg", "wolf", "theaf", "goblin",]

nameem = random.choice(names)
enemdmg = random.randint(1, 15)
enemhp = random.randint(25, 90)


player = input("What is your name? ")


strp = 0
hpp = 0
dexp = 0
upp = 10
while upp > 0:
    thing = input(f"You have {upp} points. Strength (1), Health (2), Dexterity (3): ")
    if thing == "1":
        strp += 1
        upp -= 1
    elif thing == "2":
        hpp += 1
        upp -= 1
    elif thing == "3":
        dexp += 1
        upp -= 1
    else:
        print("Invalid choice!")
strth= strp*5
hp= 20+hpp*20
raning = dexp + 2
enehp = enemhp
print(f"\n{player}, you are fighting a {nameem}!")
print(f"Enemy health: {enehp}")
print(f"Enemy damage: {enemdmg}")
def run():
    return random.randint(1, raning)
def thing():
    global hp, enehp #had help from google idk what global dose
    print(f"\nyour health: {hp}")
    print(f"enemy health: {enehp}")
    attack= input("attack (1), heal (2), flee (3), defend (4): ")
    if attack== "1":
        damage =random.randint(1, 5) + strth
        enehp -=damage
        print(f"you hit for {damage} damage!")
    elif attack== "2":
        hp+= 5
        print("you healed 5 health!")
    elif attack=="3":
        if run()==1:
            print("you escaped!")
            return"flee"
        else:
            print("you failed to escape!")
    elif attack=="4":
        print("you are defending")
        return"defend"
    else:
        print("not right choice")
    return"continue"
def montu(defend):
    global hp
    if run()== 1:
        print("You dodged the attack!")
    else:
        damage=enemdmg
        if defend:
            damage=damage // 2
        hp-=damage
        print(f"The {nameem} dealt {damage} damage!")
first = random.choice(["player", "monster"])
while hp > 0 and enehp > 0:
    if first == "monster":
        montu(False)
        first = "player"
    if hp <= 0 or enehp <= 0:
        break
    result = thing()
    if result == "flee":
        break
    if enehp <= 0:
        break
    montu(result == "defend")
if enehp <= 0:
    print("You won!")
elif hp <= 0:
    print("You lost!")