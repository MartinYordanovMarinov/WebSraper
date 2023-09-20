from Shared.Defines import WEBSITE_URL
from Shared.WebScrapper import WebScraper

import argparse


parser = argparse.ArgumentParser()
web_scraper = WebScraper(WEBSITE_URL)

parser.add_argument("-b", type=int, help="Number of books to be scraped")
parser.add_argument("-g", type=str, help="Genre to be scraped")
args = parser.parse_args()

if args.b is not None:
    if args.g is not None:
        print(web_scraper.scrape_books(args.b, web_scraper.scrape_by_genre(args.g)))
    else:
        print(web_scraper.scrape_books(args.b))
        # book_manager.add_books(web_scraper.scrape_books(args.b))
        # for book in book_manager.books:
        #     print(book)
else:
    print("Number of books arguement is required!")

