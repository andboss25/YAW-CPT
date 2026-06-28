from urllib.parse import SplitResult
from colorama import Fore

# This module is made to detect if the link might be some sort of CSS/CDN or media import

style_extensions = [
    '.css',
    '.ico','.png','.jpg','.jpeg','.webp',
    '.mp4','.avif','.mov',
    '.wav','.mp3','.m4a'
]

style_keywords = [
    'cdn','css'
]

def scan(root_url : str, parsed_url : SplitResult, url_data : dict[str], display_prefrences: dict[str]) -> dict[str]:
    # TODO expand with details such is_cdn and is_image
    url_data['is_style'] = False
    has_style_keywords = any([keyword in root_url for keyword in style_keywords])
    has_style_extensions = any([parsed_url.path.endswith(extension) for extension in style_extensions])

    if has_style_extensions or has_style_keywords:
        url_data['is_style'] = True
    
    if display_prefrences['debug'] == True:
        print(f"URL: {url_data['url']} -> IS_STYLE: {url_data['is_style']}")
    return url_data

def show_results(data:dict[str],prefrences:dict[str]):
    print("+ The ones found that are for style:")
    for link in data:
        if link['is_style'] == True:
            print(f"{Fore.LIGHTCYAN_EX}{link['url']}{Fore.WHITE}")

def show_header(data:dict[str],prefrences:dict[str]):
    style_links = [x for x in data if x['is_style'] == True]
    print(f"{Fore.CYAN}{len(style_links)}{Fore.WHITE} style links found!")