from urllib.parse import SplitResult

# This module is made to detect if the link belongs to a common social network

SOCIAL_NETLOCS = [
    # Meta
    "facebook.com",
    "www.facebook.com",
    "m.facebook.com",
    "fb.com",
    "instagram.com",
    "www.instagram.com",
    "threads.net",
    "www.threads.net",

    # X / Twitter
    "twitter.com",
    "www.twitter.com",
    "x.com",
    "www.x.com",

    # Google
    "youtube.com",
    "m.youtube.com",
    "www.youtube.com",
    "youtu.be",

    # TikTok
    "tiktok.com",
    "www.tiktok.com",

    # Reddit
    "reddit.com",
    "www.reddit.com",
    "old.reddit.com",

    # LinkedIn
    "linkedin.com",
    "www.linkedin.com",

    # Pinterest
    "pinterest.com",
    "www.pinterest.com",

    # Snapchat
    "snapchat.com",
    "www.snapchat.com",

    # Discord
    "discord.com",
    "www.discord.com",
    "discord.gg",

    # Twitch
    "twitch.tv",
    "www.twitch.tv",

    # Telegram
    "t.me",
    "telegram.me",
    "telegram.org",

    # WhatsApp
    "wa.me",
    "chat.whatsapp.com",
    "whatsapp.com",

    # Signal
    "signal.me",

    # Bluesky
    "bsky.app",

    # Mastodon
    "mastodon.social",

    # Tumblr
    "tumblr.com",
    "www.tumblr.com",

    # Flickr
    "flickr.com",
    "www.flickr.com",

    # Medium
    "medium.com",
    "www.medium.com",

    # Quora
    "quora.com",
    "www.quora.com",

    # VK
    "vk.com",
    "www.vk.com",

    # Weibo
    "weibo.com",
    "www.weibo.com",

    # LINE
    "line.me",

    # WeChat
    "wechat.com",
    "weixin.qq.com",

    # GitHub (often treated as a social coding platform)
    "github.com",
    "www.github.com",

    # GitLab
    "gitlab.com",

    # Steam Community
    "steamcommunity.com",

    # DEV Community
    "dev.to",

    # Behance
    "behance.net",
    "www.behance.net",

    # Dribbble
    "dribbble.com",
    "www.dribbble.com",
]

def scan(root_url : str, parsed_url : SplitResult, url_data : dict[str], display_prefrences: dict[str]) -> dict[str]:
    url_data['common_social'] = False

    if parsed_url.netloc in SOCIAL_NETLOCS:
        url_data['common_social'] = True
    
    if display_prefrences['debug'] == True:
        print(f"URL: {url_data['url']} -> COMMON SOCIAL: {url_data['common_social']}")
    
    return url_data

def show_results(data:dict[str],prefrences:dict[str]):
    pass

def show_header(data:dict[str],prefrences:dict[str]):
    pass