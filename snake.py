# snake water Gun

i = 0
count = 0
while i < 10:

    import random
    x = input("Enter your choice")

    y = ["snake", "water", "gun"]
    z = (random.choice(y))
    if x == "snake":
        if z == "water":
            print("snake > water: You Won")
        elif z == "gun":
            print("snake<gun: You lost!")
        elif z == "snake":
            print("Tie ")
    elif x == "water":
        if z == "snake":
            print("snake > water: You Lost ")
        elif z == "gun":
            print("water>gun: You Won!")
        elif z == "water":
            print("Tie ")
    elif x == "gun":
        if z == "snake":
            print("snake < gun: You Won")
        elif z == "water":
            print("water>gun: You lost!")
        elif z == "gun":
            print("Tie ")
    i = i+1
