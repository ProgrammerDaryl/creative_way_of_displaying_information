import pyfiglet
from colorama import Fore

# pseudocode

# request the user to enter his or her name
name = input("\033[92m Enter your name here: ")

# request the user to enter his or her dream job
dream_job = input("\033[91m Enter your dream job here: ")

# request the user to enter his or her age
age = input("\033[0;36;47m Enter your age here: ")

# request the user to enter his or her place of birth
place_of_birth = input("\033[0;35;47m Enter your place of birth here: ")

# request the user to enter his or her religion
religion = input("\033[1;36;40m Enter your religion here: ")

# print his or her name in a creative way
styled_name = pyfiglet.figlet_format("Hi, I'm " + name + "!", font = "doom")
print(Fore.CYAN + styled_name)

# print his or her dream job in a creative way
styled_dream_job = pyfiglet.figlet_format("My dream job is to become a " + dream_job + "!", font = "doom")
print(Fore.CYAN + styled_dream_job)

# print his or her age in a creative way
styled_age = pyfiglet.figlet_format("I am " + age + " years old.", font = "doom")
print(Fore.MAGENTA + styled_age)

# print his or her place of birth in a creative way
styled_place_of_birth = pyfiglet.figlet_format("From " + place_of_birth, font = "doom")
print(Fore.YELLOW + styled_place_of_birth)

# print his or her religion in a creative way
styled_religion = pyfiglet.figlet_format("My religion is " + religion + ".", font = "doom")
print(Fore.LIGHTRED_EX + styled_religion)