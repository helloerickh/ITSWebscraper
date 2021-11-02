# parse html
from bs4 import BeautifulSoup as soup
# grab page
from urllib.request import urlretrieve
# grab image
from urllib.request import urlopen as uReq
# mkdir
import os


class WebScraper:

    url = None
    html = None
    fileDirectory = None
    imgDirectory = None
    page_soup = None

    def __init__(self, urltoRead):

        # open up connection to url
        self.url = urltoRead
        u_client = uReq(urltoRead)

        # grab html from page
        self.html = u_client.read()
        u_client.close()

        os.mkdir("./files")
        os.mkdir("./images")
        self.fileDirectory = os.path.abspath("./files/")
        self.imgDirectory = os.path.abspath("./images/")

        self.page_soup = soup(self.html, "html.parser")

    def scrape(self):

        title_n_author = self.page_soup.find_all("div", class_="mp-stacks-grid-item-inner")
        images = self.page_soup.find_all("div", class_="mp-stacks-grid-item-image-holder")
        short_description = self.page_soup.find_all("div", class_="mp-stacks-postgrid-item-excerpt-holder")

        for x in range(len(title_n_author)):
            # create subdirectory for current article
            title = title_n_author[x].article.h2.text
            articleDirPath = os.path.join(self.fileDirectory, title + "/")
            os.mkdir(articleDirPath)

            # create text file for current article
            filePath = os.path.join(articleDirPath, title + ".txt")
            f = open(filePath, "w")

            # get image
            url = images[x].a.img["src"]
            imgName = url.split("/")[-1]
            imgPath = os.path.join(articleDirPath, imgName)
            urlretrieve(url, imgPath)

            # write article name
            f.write(title_n_author[x].article.h2.text + "\n\n")
            # write author name
            f.write(title_n_author[x].span.span.text + "\n\n")
            # write short description and trailing Read More
            f.write(short_description[x].div.span.text + "\n\n")
            f.write(short_description[x].div.span.span.text + "\n\n")

            f.close()
        return 0

    def scrapeImages(self):

        title_n_author = self.page_soup.find_all("div", class_="mp-stacks-grid-item-inner")
        images = self.page_soup.find_all("div", class_="mp-stacks-grid-item-image-holder")

        for x in range(len(title_n_author)):
            url = images[x].a.img["src"]
            filename = url.split("/")[-1].lower()
            imgPath = os.path.join(self.imgDirectory, filename)
            urlretrieve(url, imgPath)

        return 0
