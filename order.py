#benjmain maddux ms larose computer programing
while True:
    try:
        mon=int(input("how much mony do you have:"))
    except:
        print("try again")
    else:
        break
thing={
    "main menue":{
        "chicken": 4,
        "rice": 3,
        "pizza": 6,
        "burrito": 5,
    },
    "side":{
        "eggs": 2,
        "noodles": 7,
        "bread": 3,
    },
    "drinks":{
        "pepsi": 6,
        "water": 1,
        "dr.pepper": 2,
    }
}
print(thing)