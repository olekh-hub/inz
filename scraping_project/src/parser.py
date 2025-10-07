from bs4 import BeautifulSoup
import pandas as pd


def init_soup(html: str):
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_links(soup: BeautifulSoup):

    all_matches = soup.find("ul", class_="info-list allMatches")
    tags = all_matches.find_all("a", href=True)
    hrefs = []

    for tag in tags:
        href = tag.get("href")
        if 'match-stats' in href:
            # hrefs.append(href)
            href = href.replace('match', 'player') + "#general"
            hrefs.append(href)

    return hrefs


def get_tables(urls: list, driver):

    df = pd.DataFrame()

    for url in urls:
        specific_url = url
        driver.get(specific_url)

        html = driver.page_source
        soup = init_soup(html)

        div = soup.find("div", class_="tableWrapper all")
        table = div.find_all("table")
        df_temp = pd.read_html(str(table))[0]
        df = pd.concat([df, df_temp], axis=0)
    return df


