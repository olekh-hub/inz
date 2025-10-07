from scraper import get_page_source
from parser import get_links
from config import URL, DRIVER_PATH

if __name__ == "__main__":
    try:
        html = get_page_source(URL, DRIVER_PATH)
        matches = get_links(html)


        print(matches, len(matches), sep='\n')
        print("Well done")
    except Exception as e:
        print(e)
