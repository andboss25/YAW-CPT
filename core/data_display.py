
from colorama import Fore
from core.load_scripts import load_results_functions, load_header_functions

def display_data(data:list[dict],prefrences:dict = {}):
    print("=== [Scan results!] ===")
    print(f"{Fore.CYAN}{len(data)}{Fore.WHITE} total entrie(s) found!")

    alien_entries = [x for x in data if x['alien'] == True]
    print(f"{Fore.CYAN}{len(alien_entries)}{Fore.WHITE} alien (external) entrie(s) found!")
    
    for function in load_header_functions():
        function(data,prefrences)

    print("+ The ones found that are external:")
    for url in alien_entries:
        print(f"{Fore.GREEN}{url['url']}{Fore.WHITE}")

    for function in load_results_functions():
        function(data,prefrences)

    if prefrences['show_all_links'] == True:
        print("Here is a list of all links:")
        for link in data:
            print(link['url'])
    