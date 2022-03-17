import requests
import colorama
from colorama import Fore
import time

def scrape():
    f = open("./proxies.txt", "w+")
    proxies = open("./proxies.txt").read().splitlines()
    try:
        base_url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000"
        r = requests.get(base_url)
        for proxy in r.text.split("\n"):
            proxy = proxy.strip()
            if proxy:
                f.write(str(proxy)+"\n")
        f.close()
        print(
            f"{Fore.GREEN}[{Fore.RESET}SUCCESS{Fore.GREEN}]{Fore.RESET} Successfully Scraped Proxies"
            )
    except:
        print(
            f"{Fore.RED}[{Fore.RESET}ERROR{Fore.RED}]{Fore.RESET} Couldn't Scrape Proxies"
            )
        time.sleep(2)
        exit()
