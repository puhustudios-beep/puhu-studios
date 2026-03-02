import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode('utf-8')

html = get_html('https://www.dreamgames.com/')
soup = BeautifulSoup(html, 'html.parser')

print("HEADER:")
header = soup.find('header')
if header:
    print(header.prettify()[:1500])

print("\nFOOTER:")
footer = soup.find('footer')
if footer:
    print(footer.prettify()[:2500])
