
from colorama import Fore

def display_data(data:list[dict],prefrences:dict = {}):
    print("=== [Scan results!] ===")
    print(f"{Fore.CYAN}{len(data)}{Fore.WHITE} total entrie(s) found!")
    alien_entries = [x for x in data if x['alien'] == True]
    print(f"{Fore.CYAN}{len(alien_entries)}{Fore.WHITE} alien (external) entrie(s) found!")
    style_entries = [x for x in data if x['is_style'] == True]
    print(f"{Fore.CYAN}{len(style_entries)}{Fore.WHITE} style/(potentially) useless entrie(s) found!")
    interesting_entries = [x for x in data if x['interesting'] == True or x['potentially_interesting'] == True]
    print(f"{Fore.CYAN}{len(interesting_entries)}{Fore.WHITE} interesting or potentially interesting entrie(s) found!")

    leftovers = [ x for x in data if x['misc'] == True ]

    if prefrences['show_only_interesting'] == False:
        print("Let's go trough them all...")

    print("+ The ones found potentially interesting/interesting:")
    for url in interesting_entries:
        print(f"{Fore.LIGHTCYAN_EX}{url['url']}{Fore.WHITE}")
    
    if prefrences['show_only_interesting'] == True:
        return

    print("+ The ones found that are external:")
    for url in alien_entries:
        print(f"{Fore.GREEN}{url['url']}{Fore.WHITE}")

    print("+ The ones found that are for style:")
    for url in style_entries:
        print(f"{Fore.LIGHTMAGENTA_EX}{url['url']}{Fore.WHITE}")

    print("+ The ones found that are in neither category:")
    for url in leftovers:
        print(f"{Fore.LIGHTYELLOW_EX}{url['url']}{Fore.WHITE}")