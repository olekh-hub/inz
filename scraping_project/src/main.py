from scraper import get_page_source
from parser import init_soup, get_links, get_tables, get_match_stats
from config import URL, DRIVER_PATH

if __name__ == "__main__":
    try:
        html, driver = get_page_source(URL, DRIVER_PATH)
        soup = init_soup(html)
        matches, games = get_links(soup)
        # matches = ["https://www.footballcritic.com/premier-league-arsenal-fc-crystal-palace-fc/player-stats/3356928#general"]
        # df = get_tables(matches, driver)
        df = get_match_stats(games, driver)
        df.to_csv('match_data.csv', index=False, sep=',')
        print(df)
        print("Well done")
    except Exception as e:
        print(e)
