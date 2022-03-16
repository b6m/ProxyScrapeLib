import requests
import colorama
from colorama import Fore
import time

proxies = open("./proxies.txt").read().splitlines()

def scrape():
    f = open("./proxies.txt", "w")
    try:
        r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000")
        for proxy in r.text.split("\n"):
            proxy = proxy.strip()
            if proxy:
                f.write(str(proxy)+"\n")
        f.close()
        print(f"{Fore.GREEN}[{Fore.RESET}SUCCESS{Fore.GREEN}]{Fore.RESET} Successfully scraped proxies.")
    except:
        print(f"{Fore.RED}[{Fore.RESET}ERROR{Fore.RED}]{Fore.RESET} Unable to scrape proxies, please try again later.")
        time.sleep(2)
        exit()
