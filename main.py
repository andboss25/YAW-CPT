
import requests
import sys
import json
import os
from colorama import Fore
from requests_tor import RequestsTor

from core.link_parse import find_links
from core.data_processor import process_data
from core.data_display import display_data

already_scanned = []

def help():
    print(f" = Flags:\n{Fore.LIGHTBLACK_EX}--url {Fore.LIGHTCYAN_EX}<url>{Fore.WHITE} | url for scan\n" + 
        f"{Fore.LIGHTBLACK_EX}--tor {Fore.WHITE}| use tor as configured in config.json\n" + 
        f"{Fore.LIGHTBLACK_EX}--cache {Fore.WHITE}| TODO: implement\n" +
        f"{Fore.LIGHTBLACK_EX}--ignore-style-links {Fore.WHITE}| ignore links the tool deems as for style/javascript\n" +
        f"{Fore.LIGHTBLACK_EX}--ignore-alien-links {Fore.WHITE}| ignore links that lead to external websites\n" +
        f"{Fore.LIGHTBLACK_EX}--show-only-interesting {Fore.WHITE}| show only links the tool deems interesting\n" +
        f"{Fore.LIGHTBLACK_EX}--iter {Fore.WHITE}| set crawling iterations: default is 2\n" +
        f"{Fore.LIGHTBLACK_EX}--debug {Fore.WHITE}| various debug info such as the requests sent (recommended to use to see requests and possible bugs in real time)\n" +
        f"{Fore.LIGHTBLACK_EX}--help {Fore.WHITE}| display arguments you can use\n" )
    
def main():
    url_flag = ''
    iter_flag = 2
    use_tor = False
    ignore_alien_links = False
    show_only_interesting = False
    ignore_style_links = False
    debug = False
    cache = False

    print(f"{Fore.CYAN}Yet another web-crawler pentest tool: YAW-CPT{Fore.WHITE}")
    print(f"By {Fore.MAGENTA}@andreiplsno{Fore.WHITE}")
    print(f"{Fore.YELLOW}This tool is unpolished and various anomalies or bugs may appear, you can help this tool be better by contributing.{Fore.WHITE}")

    try:
        config = open("config.json","r")
        config = json.load(config)
    except FileNotFoundError:
        config = open("config.json","w")
        config.write("{}")
        config.close()
        config = {}


    try:
        if '--h' in sys.argv or '-h' in sys.argv or '--help' in sys.argv:
            help()
            return
        
        if '--tor' in sys.argv:
            use_tor = True

        if '--debug' in sys.argv:
            debug = True

        if '--cache' in sys.argv:
            cache = True
            # TODO IMPLEMENT

        if '--ignore-style-links' in sys.argv:
            ignore_style_links = True
            # TODO DOCUMENT

        if '--ignore-alien-links' in sys.argv:
            ignore_alien_links = True
            # TODO DOCUMENT
            # TODO IMPLEMENT

        if '--show-only-interesting' in sys.argv:
            show_only_interesting = True
            # TODO DOCUMENT
        
        if "--url" in sys.argv:
            url_flag = sys.argv[sys.argv.index("--url") + 1]

        if "--iter" in sys.argv:
            iter_flag = int(sys.argv[sys.argv.index("--iter") + 1])

    except IndexError:
        help()
        return

    if url_flag == '':
        print(f"{Fore.RED}Please provide an '--url' flag!{Fore.WHITE}")
        return
    
    display_prefrences = {
        "ignore_alien_links":ignore_alien_links,
        "ignore_style_links":ignore_style_links,
        "show_only_interesting":show_only_interesting,
        "debug":debug
    }

    if use_tor == True:
        print(f"{Fore.MAGENTA}Starting tor service from config.json file...{Fore.WHITE}")
        tor_executable_path = config.get("tor")
        if tor_executable_path == None:
            print(f"{Fore.YELLOW}No 'tor' attribute found in config.json,\nyou can put the path to tor there to automatically start the executable!\nRelying on you to start tor yourself!{Fore.WHITE}")
        else:
            os.startfile(tor_executable_path)

        input(f"Press {Fore.CYAN}enter{Fore.WHITE} when the tor executable has started!")
        tor_requests = RequestsTor(tor_ports=(9050,), tor_cport=9051)
        tor_ip = tor_requests.check_ip()
        print(f"Using ip {Fore.MAGENTA}{tor_ip}{Fore.WHITE}")
        scan(url_flag,0,tor_requests,url_flag,iter_flag,display_prefrences)
    else:
        scan(url_flag,0,requests,url_flag,iter_flag,display_prefrences)

def scan(url,iteration:int,request_library : requests,root_loc:str,max_iter,display_prefrences:dict = {}):
    request_data : requests.Response = None
    iteration += 1
    try:
        if url in already_scanned:
            return []
        request_data = request_library.get(url)
        already_scanned.append(url)
        if display_prefrences['debug'] == True:
            print(f"GET {url} => {request_data.status_code} iter:{iteration} out of {max_iter}")
    except Exception as e:
        print(f"{Fore.RED}Error at link {url} {str(e)}!{Fore.WHITE}")
        return []
    
    # TODO ADD CACHING OF DATA
    
    results = find_links(request_data.text)
    
    processed_results = process_data(results,root_loc)

    if display_prefrences['ignore_style_links']:
        processed_results = [x for x in processed_results if x['is_style'] == False]

    if display_prefrences['ignore_alien_links']:
        processed_results = [x for x in processed_results if x['alien'] == False]

    if iteration >= max_iter:
        return []

    for x in processed_results:
        processed_results.extend(scan(x['url'],iteration,request_library,root_loc,max_iter,display_prefrences))

    if iteration == 1:
        # TODO REMOVE ALL DUPLICATES BY FINAL PROCESSING
        display_data(processed_results,display_prefrences)

    return processed_results

if __name__ == "__main__":
    main()