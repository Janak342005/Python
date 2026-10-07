import random
from colorama import Fore, Style,init
init(autoreset=True)

# userLevel = 1;

# randomNumber = random.randint(1,userLevel*10);

# userAnswer = int(input(f"Guesse a number between 1 to {userLevel*10} :-"))

# attempts = 1;

# maxAttempts = 5;

# while attempts < maxAttempts:
#     if randomNumber == userAnswer:
#         print(Fore.GREEN + "You got it right")
#         print(Fore.LIGHTCYAN_EX + f"you got it in {attempts} attempts only. ")
#         userLevel += 1;
#         break

#     elif randomNumber < userAnswer:
#         print(Fore.YELLOW + "You got it higher think lower")
#         userAnswer = int(input("Take another guesse :- "))

#     elif randomNumber > userAnswer:
#         print(Fore.BLUE + "You got it lower think higher")
#         userAnswer = int(input("Take another guesse :- "))


#     attempts += 1;

# else:
#    print(Fore.RED + "You ran out of attempts")
#    print(f"Answer was {randomNumber}");




randomString = ["janak","rashi","penguine","raja"]

print(random.choice(randomString));