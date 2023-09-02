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
        if response != 404 and valide:
            return True
    except Exception:
        print(f"{Fore.RED}[x]{Fore.WHITE} You provided an invalid URL. Please put a valid URL like this example: https://example com")
        return False


# scan web technologies present on the target
def scan_techno(elements_list, website):
    techno = open("techno.txt", "w", encoding="utf-8")

    for description, data in website.items():
        elements_list.append(f"{description}: ")
        elements_list.extend(data)

    for i in range(0, len(elements_list), 2):
        result_scan_techno = elements_list[i] + elements_list[i + 1]
        print(f"{Fore.BLUE}[*]{Fore.WHITE} {result_scan_techno}")
        techno.write(result_scan_techno+"\n")

    techno.seek(0)
    techno.close()


if check_url(url):
    scan_techno(elements_list, website)
    print(f"{Fore.GREEN}[+]{Fore.WHITE} You can view the report on index.html...")