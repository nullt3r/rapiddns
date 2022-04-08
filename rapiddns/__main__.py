import requests
import argparse
import logging
import time
from bs4 import BeautifulSoup

class RapidDns:
    @staticmethod
    def __extract_items(url):
        items = []

        try:
            request = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"})
            html = request.content
        except Exception as e:
            logging.error(
                "there was an error while reaching rapiddns.io: %s", e
            )
            return

        if request.status_code != 200:
            logging.error(
                "there was an error while reaching the rapiddns.io, the server responded with non-200 satus code"
            )
            return

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
            return


        return items[1:]
    
    @classmethod
    def getSubdomains(cls, domain):
        url = f"https://rapiddns.io/subdomain/{domain}?full=1&down=1"
        return cls.__extract_items(url)
    
    @classmethod
    def ipToDomains(cls, ip):
        url = f"https://rapiddns.io/s/{ip}?full=1&down=1"
        return cls.__extract_items(url)


def main():
    from rapiddns import __version__

    parser = argparse.ArgumentParser(description=f"rapiddns v{__version__.__version__} - a simple python client for rapiddns.io by @nullt3r")

    parser.add_argument(
        "--subdomains",
        "-s",
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
    parser.add_argument(
        "--full",
        action="store_true",
        help="full output with detailed information",
        required=False,
    )

    args = parser.parse_args()

    arg_subdomains = args.subdomains
    arg_ip = args.ip
    arg_full = args.full

    if (arg_subdomains or arg_ip) is None:
        parser.error('parameter --subdomains or --ip is required. You can specify both.')

    if arg_subdomains is not None:
        if arg_full is True:
            for line in RapidDns.getSubdomains(arg_subdomains):
                print(" ".join(line))
        else:
            subdomains = [resource[0] for resource in RapidDns.getSubdomains(arg_subdomains)]
            print("\n".join(set(subdomains)))

    if arg_ip is not None:
        if arg_full is True:
            for line in RapidDns.ipToDomains(arg_ip):
                print(" ".join(line))
        else:
            domains = [resource[0] for resource in RapidDns.ipToDomains(arg_ip)]
            print("\n".join(set(domains)))

if __name__ == "__main__":
    main()