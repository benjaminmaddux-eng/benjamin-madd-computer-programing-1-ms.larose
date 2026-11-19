#benjmain maddux ms larose computer programing
thing = {
    "main menu": {
        "chicken": 4,
        "rice": 3,
        "pizza": 6,
        "burrito": 5
    },
    "side": {
        "eggs": 2,
        "noodles": 7,
        "bread": 3,
        "fries": 3
    },
    "drinks": {
        "pepsi": 6,
        "water": 1,
        "dr.pepper": 2,
        "lemonade": 3
    }
}
def chose(meu, cat):
    while True:
        print("\nchose a", cat + ":")
        for item, price in meu.items():
            print(item, "- $", price)
        choce=input("your choice: ").lower()
        if choce in meu:
            return choce
        else:
            print("thats not on the menue")
print("welcome to the restuant!")
print("\nFULL MENU")
for cat, menu in thing.items():
    print("\n",cat)
    for item,price in menu.items():
        print(item, "- $", price)
drink=chose(thing["drinks"], "drink")
main= chose(thing["main menu"], "main course")
side1=chose(thing["side"], "first side")
side2=chose(thing["side"], "second side")
tot=thing["drinks"][drink]
tot=tot +thing["main menu"][main]
tot=tot + thing["side"][side1]
tot= tot +thing["side"][side2]
print("\nYOUR ORDER")
print("drink:", drink)
print("main:",main)
print(f"side: {side1} {side2}")
print("total cost: $", format(tot,".2f"))