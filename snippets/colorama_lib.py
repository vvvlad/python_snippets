from colorama import Fore, Back, Style


print(Fore.YELLOW)
print("This is a warning!")

print(Back.RED + Fore.WHITE + "This is an error!")

print(Back.RESET + Style.DIM + "Another error!")

print(Style.RESET_ALL)
print("Back to normal")