import requests
import argparse
import logging
import time
from bs4 import BeautifulSoup

class RapidDns:
    @staticmethod
    def __extract_items(url):
        items = []
        for i in range(5):
            try:
                request = requests.get(url)
                html = request.content
            except Exception as e:
                logging.error(
                    "there was an error while reaching rapiddns.io: %s", e
                )
                time.sleep(5)
                continue

            if request.status_code != 200:
                logging.error(
                    "there was an error while reaching the rapiddns.io, the server is down? Trying again..."
                )
                time.sleep(5)
                continue

            try:
                soup = BeautifulSoup(html, "html.parser")
                table = soup.find("table", id="table")
                rows = table.findAll("tr")
                items = []
                for row in rows:
                    cells = row.findAll("td")
                    items.append([value.text.strip() for value in cells])
            except Exception as e:
                logging.error(
                    "can't extract data from rapiddns.io, reason: %s", e
                )
                continue

        return items[1:]
    
    @classmethod
    def getSubdomains(cls, domain):
        url = f"https://rapiddns.io/s/{domain}?full=1&down=1"
        return cls.__extract_items(url)
    
    @classmethod
    def ipToDomains(cls, domain):
        url = f"https://rapiddns.io/s/{domain}?full=1&down=1"
        return cls.__extract_items(url)


def main():
    parser = argparse.ArgumentParser(description="rapiddns - a simple python client for rapiddns.io by @nullt3r")

    parser.add_argument(
        "-s",
        "--subdomains",
        action="store",
        help="expecting a domain name",
        required=False,
    )
    parser.add_argument(
        "--ip",
        action="store",
        help="expecting an IP adress or CIDR",
        required=False,
    )

    args = parser.parse_args()

    arg_subdomains = args.subdomains
    arg_ip = args.ip

    if not (arg_subdomains or arg_ip):
        parser.error('parameter --subdomains or --ip is required. You can specify both.')

    if arg_subdomains is not None:
        for value in RapidDns.getSubdomains(arg_subdomains):
            print(value[0])
    
    if arg_ip is not None:
        for value in RapidDns.ipToDomains(arg_ip):
            print(value[0])     

if __name__ == "__main__":
    main()