import requests
import bs4
r = requests.get("https://www.kicker.de/2-bundesliga/tabelle")
print(r)
soup = bs4.BeautifulSoup(r.content, 'html.parser')
tbody = soup.find("tbody")
tfList = soup.find_all("tbody", recursive=True)
print(type(tfList))