# Choose your own adventure game:- Terminal based written in python.
# How to progrese in the game
#User starts by chossing their character then choose between different scenario out of which only one path is right and rest all leads to the end of the player.
# Characters in game are farmer, king, knight, monkey.

# We start by making the characters, and setting up the layer intro to the game.

gameCharKing = {
    "name": "King".upper(),
    "Power": int(100),
    "score" : int(100),
    "GameLength": int(4),

}

gameCharKnight = {
    "name": "Knight".upper(),
    "Power": int(50),
    "GameLength": int(4),
}

gameCharFarmer = {
    "name": "Farmer".upper(),
    "Power": int(30),
    "GameLength": int(4),
}

gameCharMonkey = {
    "name": "Monkey".upper(),
    "power": int(10),
    "GameLength": int(4),
}



# With game characters made now we need to assign each of them their story
# The game will have four questions and a mega vilian based on the answers we give or take power stats of the player and at the end if he has earned enough power he can win the game or else loose.


chooseYourPlayer = str(input("Choose your character: King , Farmer, Knight, Monkey :- "+" ")).upper();

if gameCharKing["name"] == chooseYourPlayer or gameCharFarmer["name"] == chooseYourPlayer or gameCharKnight["name"] == chooseYourPlayer or gameCharMonkey["name"] == chooseYourPlayer:
    print(f"The user has choosen this char {chooseYourPlayer}");
else:
    print("Choose thang se yaar");


if chooseYourPlayer == gameCharKing["name"]:
    userQueOne = int(input("If you want to kill dragon how much army will you use? :- (10,20,40,50) :-"+" "));
    if userQueOne == 40:
        print("Itni army yaha use karega to barbad nahi ho jayega.");
        userQueTwo = int(input("Ab batao farmer ko kitne paise donge? :-  100, 1000, 500, 2000 (2300 funds available. :- )"))
        gameCharKing = {
        "power": int(80),
        }

    if userQueOne == 10:
        print("Dragon hai woh tumhare chacha ka ladka nahi");
        gameCharKing = {
            "power" : int(80),
        }
        userQueTwo = int(input("Ab batao farmer ko kitne paise donge? :-  100, 1000, 500, 2000 (2300 funds available. :- )"))
        
    if userQueOne == 20:
        print("Ab ki na thodi akal mando wali baat")
        gameCharKing = {
            "power" : int(120),
        }
        userQueTwo = int(input("Ab batao farmer ko kitne paise donge? :-  100, 1000, 500, 2000 (2300 funds available. :- )"))

        if userQueTwo == 500:
            print("Very good Mar do tum praja ko bhuka rakh ke.")
        if userQueTwo == 100:
            print("Bhai ye bhi kyu hi de raha hai")
        if userQueTwo == 1000:
            print("Acha raja banaga re tu")
        if userQueTwo == 2000:
            print("Desh chala raha hai ya dabha")
        
    if userQueOne == 50:
        print("Raja kisne banaya tujhe")
        userQueTwo = int(input("Ab batao farmer ko kitne paise donge? :-  100, 1000, 500, 2000 (2300 funds available. :- )"))
        gameCharKing = {
            "power": int(80),
        }




else:
    print("xyz")