from scraper import get_page_source
from parser import init_soup, get_links, get_tables
from config import URL, DRIVER_PATH

if __name__ == "__main__":
    try:
        html, driver = get_page_source(URL, DRIVER_PATH)
        soup = init_soup(html)
        matches = get_links(soup)
        df = get_tables(matches, driver)
        df.to_csv('data.csv', index=False, sep=';')

        print("Well done")
    except Exception as e:
        print(e)
