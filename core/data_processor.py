import sys
from urllib.parse import urlsplit
import core.load_scripts

sys.dont_write_bytecode = True


def process_data(results:list[str],root_loc:str,display_prefrences:dict):
    detection_functions = core.load_scripts.load_scan_functions()
    root_netloc = urlsplit(root_loc).netloc
    root_scheme = urlsplit(root_loc).scheme

    data = []

    for url in results:
        # Basic scan before scripted scan
        this_url = {}
        parsed_url = urlsplit(url)

        this_url['url'] = url

        if parsed_url.netloc == '':
            this_url['alien'] = False
            this_url['url'] = root_scheme + "://" + root_netloc + url
        elif parsed_url.netloc == root_netloc:
            this_url['alien'] = False
        else:
            this_url['alien'] = True

        if parsed_url.query != '':
            this_url['has_query'] = True
        else:
            this_url['has_query'] = False

        data.append(this_url)

        # Advanced scan
        for scan_function in detection_functions:
            this_url = scan_function(url,parsed_url,this_url,display_prefrences)
        
        
    return data

def post_process(links:list[dict]):
    link_list = {}
    data_pool = []
    for link in links:
        if link_list.get(link['url']) == None:
            data_pool.append(link)
            link_list[link['url']] = True
        else:
            pass

    return data_pool

        