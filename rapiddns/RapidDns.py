import requests
from bs4 import BeautifulSoup

from rapiddns import Exceptions

def __extract_items(url):
    items = []

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"})
        html = response.content
    except Exception as e:
        raise Exceptions.RapidDnsNetworkError("can't connect to rapiddns.io")

    if response.status_code != 200:
        raise Exceptions.RapidDnsHTTPError("there was an error while reaching the rapiddns.io, the server responded with non-200 satus code")

    try:
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", id="table")
        rows = table.findAll("tr")
        items = []
        for row in rows:
            cells = row.findAll("td")
            items.append([value.text.strip() for value in cells])
    except Exception as e:
        raise Exceptions.RapidDnsHTMLParserError("can't parse HTML data from rapiddns.io")

    return items[1:]

def subdomains(domain):
    url = f"https://rapiddns.io/subdomain/{domain}?full=1&down=1"
    return __extract_items(url)

def sameip(ip):
    url = f"https://rapiddns.io/s/{ip}?full=1&down=1"
    return __extract_items(url)


