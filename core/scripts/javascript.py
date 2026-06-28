from urllib.parse import SplitResult
from colorama import Fore

# This module is made to detect if the link might be some sort of javascript
extensions = [
    '.js','.min.js','.ts'
]

keywords = [
    'javascript','script','jquery'
]

def scan(root_url : str, parsed_url : SplitResult, url_data : dict[str], display_prefrences: dict[str]) -> dict[str]:
    url_data['is_js'] = False
    has_keywords = any([keyword in root_url for keyword in keywords])
    has_extensions = any([parsed_url.path.endswith(extension) for extension in extensions])

    if has_extensions or has_keywords:
        url_data['is_js'] = True
    
    if display_prefrences['debug'] == True:
        print(f"URL: {url_data['url']} -> IS_JS: {url_data['is_js']}")
    return url_data

def show_results(data:dict[str],prefrences:dict[str]):
    print("+ The ones found that are detected as javascript:")
    for link in data:
        if link['is_js'] == True:
            print(f"{Fore.MAGENTA}{link['url']}{Fore.WHITE}")

def show_header(data:dict[str],prefrences:dict[str]):
    links = [x for x in data if x['is_js'] == True]
    print(f"{Fore.CYAN}{len(links)}{Fore.WHITE} javascript links found!")