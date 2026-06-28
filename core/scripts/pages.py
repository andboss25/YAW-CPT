from urllib.parse import SplitResult
from colorama import Fore

# This module is made to detect if the link might be some sort of CSS/CDN or media import

style_extensions = [
    '.html'
]

style_keywords = [
    'about','home','login','signup','privacy','policy'
]

def scan(root_url : str, parsed_url : SplitResult, url_data : dict[str], display_prefrences: dict[str]) -> dict[str]:
    # TODO expand with details such is_cdn and is_image
    url_data['is_page'] = False
    has_style_keywords = any([keyword in root_url for keyword in style_keywords])
    has_style_extensions = any([parsed_url.path.endswith(extension) for extension in style_extensions])

    has_other_tropes = False
    for x in url_data['url']:
        for x in ['css','api','style','js','internal','javascript','m4a']:
            if x in url_data['url']:
                has_other_tropes = True

    if ( has_style_extensions or has_style_keywords ) and not has_other_tropes:
        url_data['is_page'] = True
    
    if display_prefrences['debug'] == True:
        print(f"URL: {url_data['url']} -> is_page: {url_data['is_page']}")
    return url_data

def show_results(data:dict[str],prefrences:dict[str]):
    print("+ The ones found that are detected as pages:")
    for link in data:
        if link['is_page'] == True:
            print(f"{Fore.YELLOW}{link['url']}{Fore.WHITE}")

def show_header(data:dict[str],prefrences:dict[str]):
    style_links = [x for x in data if x['is_page'] == True]
    print(f"{Fore.CYAN}{len(style_links)}{Fore.WHITE} page links found!")