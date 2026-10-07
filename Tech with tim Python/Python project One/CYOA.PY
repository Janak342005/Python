# Choose your own adventure game:- Terminal based written in python.
# How to progrese in the game
#User starts by chossing their character then choose between different scenario out of which only one path is right and rest all leads to the end of the player.
# Characters in game are farmer, king, knight, monkey.

# We start by making the characters, and setting up the layer intro to the game.

gameCharKing = {
    "name": "King".upper(),
    "Power": int(100),
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
    if userQueOne == 10:
        print("Dragon hai woh tumhare chacha ka ladka nahi");
    if userQueOne == 20:
        print("Ab ki na thodi akal mando wali baat")
    if userQueOne == 50:
        print("Raja kisne banaya tujhe")


else:
    print("xyz")