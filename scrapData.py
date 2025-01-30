import requests
import bs4

def scrap(link):
    link = link.strip("\n")
    r = requests.get(link)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    tbody = soup.find("tbody")
    rows = tbody.find_all("tr")
    listRows = []
    for row in rows:
        cols = row.find_all("td")
        cols = [col.get_text(strip=True) for col in cols]
        listRows.append(cols)
    return listRows

