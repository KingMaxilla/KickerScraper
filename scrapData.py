import requests
import bs4
r = requests.get("https://www.kicker.de/2-bundesliga/tabelle")
soup = bs4.BeautifulSoup(r.content, 'html.parser')
tbody = soup.find("tbody")
rows = tbody.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    cols = [col.get_text(strip=True) for col in cols]
    

