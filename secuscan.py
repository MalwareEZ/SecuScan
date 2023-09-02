#!/usr/bin/python3
import builtwith
import argparse
import requests
import validators
from colorama import Fore
from datetime import datetime

parser = argparse.ArgumentParser(description="Tool for pentest")
parser.add_argument("-u", "--url", dest="url", help="Ex: --url http://example.com", required=True)
args = parser.parse_args()

url = args.url
elements_list = []
website = builtwith.parse(url)

# information report
def report():
    current_dateTime = datetime.now()
    return current_dateTime.strftime("%d %B %Y")


# Check if the url is valid
def check_url(url):
    try:
        response = requests.get(url)
        valide = validators.url(url)
        
        if response.status_code != 404 and valide:
            return True
    
    except Exception:
        print(f"{Fore.RED}[x]{Fore.WHITE} You provided an invalid URL. Please put a valid URL like this example: https://example.com")
        return False


def scan_techno(elements_list, website):
    for description, data in website.items():
        result_techno = f"{description}: {', '.join(data)}"
        elements_list.append(result_techno)

    with open("techno.txt", "w", encoding="utf-8") as techno_file:
        techno_file.write('\n'.join(elements_list))


if check_url(url):
    scan_techno(elements_list, website)
    print(f"{Fore.GREEN}[+]{Fore.WHITE} You can view the report in techno.txt...")
