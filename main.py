from ITSScraper import WebScraper

def main():

    url = "https://its.sdsu.edu/news/"

    test = WebScraper(url)
    test.scrape()
    test.scrapeImages()


if __name__ == "__main__":
    main()
