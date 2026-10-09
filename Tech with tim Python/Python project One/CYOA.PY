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

gameScore = 100;

def userQueOneKing():
    userQueOne = int(input("Dragon ko marne ke liye kitni army use karoge? (20,40,10,80) :- "));
    if userQueOne == 20:
        print("Bhai dragon hai tere chahcha ka ladka nahi.");
        gameScore =- 20;
    elif userQueOne == 40:
            print("Bhai ye ki na raja wali baat");
            gameScore =+ 30;
    elif userQueOne == 10:
            print("Bhai ye bhi kyu bhej raha hai");
            gameScore =- 20;
    elif userQueOne == 80:
            print("Bhai sab kuch yaha use kar lega to rajya kaise chalyeg.");
            gameScore =- 20;
    else:
        print("Bhai aankho ka illaj karwa le.")

def userQueTwo():
    userQueTwo = int(input("Ab batao farmer ko kitne paise donge? :-  100, 1000, 500, 2000 (2300 funds available. :- )"))
    
    if userQueTwo == 500:
        print("Very good Mar do tum praja ko bhuka rakh ke.");
        gameScore =- 40;
    elif userQueTwo == 100:
                print("Bhai ye bhi kyu hi de raha hai")
                gameScore =- 40;
    elif userQueTwo == 1000:
                print("Acha raja banaga re tu")
                gameScore =+ 50;
    elif userQueTwo == 2000:
                print("Desh chala raha hai ya dabha")
                gameScore =- 40;

def userQueThree():
    userQueThree = int(input("Knight ko salary kitni doge? (200,500,2000,1000):- {Available defence budget is: 2300}"));
    if userQueThree == 200:
        print("Bhai tera knight hai koi bandar nahi")
        gameScore =- 15;
    elif userQueThree == 500:
        print("Chal aacha hai lekin bhai isme woh bhuka mar jayega")
        gameScore =- 10;
    elif userQueThree == 1000:
        print("Very good ab tu dragon se lad payega (Que 1)")
        gameScore =+ 25;
    else:
        print("Haa bhai tu sab isko hi dede. Egoist kahi ke.")
        gameScore =- 15;



if chooseYourPlayer == gameCharKing["name"]:
        print(f"User has chosen {chooseYourPlayer}");
        userQueOneKing();
        userQueTwo();
        userQueThree();
        if gameScore<100:
            print("Haar gaye aap janab please kabhi prime minister mat banna.")
        else:
            print(gameScore)