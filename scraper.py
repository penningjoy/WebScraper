'''
Program - Web Scraper
Developer - Joydeep Banerjee
Description - The program is built to scrape a test site - 
              https://webscraper.io/test-sites/e-commerce/allinone . The scraper
              is built using Python libraries requests and BeautifulSoup. The library
              BeautifulSoup really makes it easy to parse through HTML pages and scrape
              content off them. In this case, the scraped off data is dumped in a CSV file
              inside the working directory.
'''

import requests
import csv
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        self.itemlist = []
        self.URL = "https://webscraper.io/test-sites/e-commerce/allinone"

    def scrapedItems(self):
        try:
            page = requests.get(url = self.URL) # Get the page content
            soup = BeautifulSoup(page.text, 'html.parser')
            # Get the child content of div class='thumbnail'
            items = soup.findAll('div', class_='thumbnail') 

            for item in items:
                itemdict = {}
                itemdict["name"] = item.contents[3].contents[5].string
                itemdict["price"] = item.contents[3].contents[1].string
                self.itemlist.append(itemdict)

            return self.itemlist

        except:
            print("Something went wrong while the scraping")



    def writeToFile(self, itemlist):
        
        #The scraped data will be dumped into the items.csv file
        # inside this working directory. The file is either created or
        # overwritten, if already present everytime the program is run.
        with open('items.csv', mode='w') as item_file:
            item_writer = csv.writer(item_file, delimiter=',', 
                                     quotechar='"', quoting=csv.QUOTE_ALL)
            for everyItem in itemlist:
                item_writer.writerow( [everyItem["name"], everyItem["price"]])



def main():
    scraper = Scraper()
    items = scraper.scrapedItems()

    if(len(items) > 0):
        scraper.writeToFile(items)

if __name__ == "__main__":
    main()


