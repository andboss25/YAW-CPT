
from urllib.parse import urlsplit

def process_data(results:list[str],root_loc:str):
    style_extensions = [
        '.css','.js',
        '.ico','.png','.jpg','.webp',
        '.mp4','.avif','.mov',
        '.wav','.mp3'
    ]

    style_keywords = [
        'cdn','javascript','css','js'
    ]

    potentially_interesting_extensions = [
        '.json','.xml'
        '.pdf','.docx'
    ]

    interesting_extensions = [
        '.php','.aspx','.db'
    ]

    interesting_keywords = [
        'api','admin'
    ]

    root_netloc = urlsplit(root_loc).netloc
    root_scheme = urlsplit(root_loc).scheme

    data = []

    for url in results:
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

        if any(elem in parsed_url.path for elem in style_extensions) or any(elem in url for elem in style_keywords):
            this_url['is_style'] = True
        else:
            this_url['is_style'] = False

        if any(elem in parsed_url.path for elem in potentially_interesting_extensions):
            this_url['potentially_interesting'] = True
        else:
            this_url['potentially_interesting'] = False

        if any((elem in parsed_url.path for elem in interesting_extensions ) or ( interesting_keywords in url )):
            this_url['interesting'] = True
        else:
            this_url['interesting'] = False

        if this_url['interesting'] == False and this_url['alien'] == False and this_url['is_style'] == False and this_url['potentially_interesting'] == False:
            this_url['misc'] = True
        else:
            this_url['misc'] = False


        data.append(this_url)
    return data