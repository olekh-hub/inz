from bs4 import BeautifulSoup


def get_links(html: str):
    soup = BeautifulSoup(html, 'lxml')

    all_matches = soup.find("ul", class_="info-list allMatches")
    tags = all_matches.find_all("a", href=True)
    hrefs = []

    for tag in tags:
        href = tag.get("href")
        if 'match-stats' in href:
            # hrefs.append(href)
            href = href.replace('match', 'player')
            hrefs.append(href)

    return hrefs

