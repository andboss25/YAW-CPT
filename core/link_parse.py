
import re
from colorama import Fore

def find_links(data):
    results = []
    
    results.extend(re.findall(r"https://[a-zA-Z./?=0-9&-]+",data))
    results.extend(re.findall(r"'/[a-zA-Z./?=0-9&-]+'",data))
    results.extend(re.findall(r'"/[a-zA-Z./?=0-9&-]+"',data))
    # TODO add a special category for this type of string : ``
    results.extend(re.findall(r' /[a-zA-Z./?=0-9&-]+',data))

    # for some special cases
    # 'src=/link'
    equal_results = re.findall(r"=/[a-zA-Z./?=0-9&-]+",data)
    equal_results_processed = []

    for x in equal_results:
        equal_results_processed.append(x.lstrip("="))
    
    results.extend(equal_results_processed)

    # src='/link otherlink'
    results.extend(re.findall(r"'/[a-zA-Z./?=0-9&-]+",data))
    results.extend(re.findall(r'"/[a-zA-Z./?=0-9&-]+',data))


    results = [x.strip("'") for x in results]
    results = [x.strip('"') for x in results]
    results = [x.strip(' ') for x in results]

    doubleslash_anomaly = []
    for x in results:
        if x.startswith("//"):
            # not the best way to fix this but meh
            doubleslash_anomaly.append(f"https:{x}")
            results.remove(x)
    
    results.extend(doubleslash_anomaly)
            
    results = list(set(results))
    return results

if __name__ == "__main__":
    test_content = open('core\\test-content\\links.html','r').read()
    results = find_links(test_content)

    links = [
        "/canonical",
        "https://example.com/alternate",
        "/css/styles.css",
        "/fonts/font.woff2",
        "https://cdn.example.com/prefetch.js",
        "https://api.example.com",
        "https://static.example.org",
        "/favicon.ico",
        "/site.webmanifest",
        "https://mysite.example/page",
        "https://twitter.example/page",
        "/refresh-target",
        "https://base.example/",
        "/images/background.jpg",
        "/cursors/cursor.cur",
        "https://images.example.com/banner.png",
        "/js/main.js",
        "/js/internal-config.json",
        "https://api.example.com/config",
        "/api/users",
        "https://jsonplaceholder.typicode.com/posts",
        "/analytics/beacon",
        "/images/runtime.png",
        "/js/dynamic.js",
        "/redirect",
        "/history-entry",
        "https://openai.com",
        "/workers/main-worker.js",
        "/home",
        "https://www.wikipedia.org",
        "/images/photo.jpg",
        "/images/photo-large.webp",
        "/images/photo-small.jpg",
        "/images/poster.jpg",
        "/media/video.mp4",
        "/media/audio.mp3",
        "/embedded/page.html",
        "/files/document.pdf",
        "/files/data.bin",
        "/submit",
        "/button-submit",
        "/map-link",
        "/images/map.jpg",
        "/svg-link",
        "/images/svg-image.png",
        "https://quotes.example.com/source",
        "/quotes/reference",
        "/history/deleted",
        "https://changes.example.com/revision",
        "/data/internal.json",
        "https://data.example.com/file.json",
        "/images/inline-background.png",
        "/images/lazy.jpg",
        "/images/src.jpg",
        "/images/src-1x.jpg",
        "https://cdn.example.com/src-2x.jpg",
        "/captions/en.vtt",
        "/images/button.png",
        "/downloads/archive.zip",
        "/ping-target",
        "https://analytics.example.com/ping",
        "/template-link",
        "/noscript-page",
        "/config/app.json",
        "https://config.example.com/app.json",
        "https://schema.org",
        "https://example.org/page",
        "/comment/internal",
        "https://comments.example.com/reference",
    ]

    if set(results) == set(links):
        print(f"{Fore.GREEN}Test 1 passed!{Fore.WHITE}")
    else:
        print(f"{Fore.RED}Test 1 failed!{Fore.WHITE}")

    
        