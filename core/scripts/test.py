from urllib.parse import SplitResult

def scan(root_url : str, parsed_url : SplitResult, url_data : dict[str], display_prefrences: dict[str]) -> dict[str]:
    if display_prefrences['debug'] == True:
        print(f"URL: {url_data['url']}")
    return url_data

def show_results(data:dict[str],prefrences:dict[str]):
    pass

def show_header(data:dict[str],prefrences:dict[str]):
    pass