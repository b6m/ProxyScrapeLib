import requests
import colorama
from colorama import Fore, init
import time
start_time = time.time()

def scrape():
    init(convert=True)
    ProxyAmount = 0
    try:

        f = open("./proxies.txt", "w+")
        base_url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000"
        r = requests.get(base_url)
        for x in r.text.split("\n"):
            x = x.strip()
            if x:
                ProxyAmount = ProxyAmount + 1 
                f.write(str(x)+"\n")
        f.close()
        print(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Sucessfully Scraped {ProxyAmount} Proxies"
            )
    except:
        print(
            f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.RESET} Could Not Scrape Proxies"
            )
        time.sleep(1.5)
        exit()
