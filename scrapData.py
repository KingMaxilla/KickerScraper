import requests
import bs4

def scrap(link):
    link = link.strip("\n")
    r = requests.get(link)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    title = soup.select_one("body > div:nth-of-type(3) > div:nth-of-type(1) > div > div:nth-of-type(3) > div > div > h1 > div > span:nth-of-type(1)")
    tbody = soup.find("tbody")
    rows = tbody.find_all("tr")
    listRows = []
    listRows.append([title.get_text(strip=True)])
    for row in rows:
        cols = row.find_all("td")
        cols = [col.get_text(strip=True) for col in cols]
        listRows.append(cols)
    return listRows

