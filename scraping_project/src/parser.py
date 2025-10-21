from bs4 import BeautifulSoup
import pandas as pd


def init_soup(html: str):
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_links(soup: BeautifulSoup):

    all_matches = soup.find("ul", class_="info-list allMatches")
    tags = all_matches.find_all("a", href=True)
    hrefs_player_stats = []
    hrefs_match_stats = []

    for tag in tags:
        href = tag.get("href")
        if 'match-stats' in href:
            # hrefs.append(href)
            href_player_stats = href.replace('match', 'player') + "#general"
            hrefs_player_stats.append(href_player_stats)
            hrefs_match_stats.append(href)

    return hrefs_player_stats, hrefs_match_stats


def get_match_stats(urls: list, driver):
    df = pd.DataFrame()

    for url in urls:
        specific_url = url
        driver.get(specific_url)

        html = driver.page_source
        soup = init_soup(html)

        match_id = url.split('/')[-1].split('#')[0]
        home_team = soup.find("div", class_="team-logo").find("img")['alt']
        away_team = soup.find('div', class_='team-logo away').find('img')['alt']
        df_temp = pd.DataFrame({'match_id': [match_id], 'home_team': [home_team], 'away_team': [away_team]})
        df = pd.concat([df, df_temp], axis=0)
    return df

# def get_tables(urls: list, driver):
#
#     df = pd.DataFrame()
#
#     for url in urls:
#         specific_url = url
#         driver.get(specific_url)
#
#         html = driver.page_source
#         soup = init_soup(html)
#
#         div = soup.find("div", class_="tableWrapper all")
#         table = div.find_all("table")
#         team = str(soup.find_all('td', class_='clubLogo cel_ALL')).split('Logo of ')[1].split('"')[0]
#         print(f'TEEEAM: {team}')
#         df_temp = pd.read_html(str(table))[0]
#         df_temp['MATCH_ID'] = url.split('/')[-1].split('#')[0]
#         df_temp['TEAM'] = team
#
#         df = pd.concat([df, df_temp], axis=0)
#     return df


def get_tables(urls: list, driver):
    df = pd.DataFrame()

    for url in urls:
        driver.get(url)
        html = driver.page_source
        soup = init_soup(html)

        div = soup.find("div", class_="tableWrapper all")
        tables = div.find_all("table")

        for table in tables:
            # Wczytaj tabelę jako DataFrame
            df_temp = pd.read_html(str(table))[0]

            team_cells = table.find_all('td', class_='clubLogo cel_ALL')
            teams = [str(cell.find('img')).split('Logo of ')[1].split('"')[0] for cell in team_cells]

            df_temp['TEAM'] = teams
            df_temp['MATCH_ID'] = url.split('/')[-1].split('#')[0]

            df = pd.concat([df, df_temp], axis=0, ignore_index=True)

    return df

