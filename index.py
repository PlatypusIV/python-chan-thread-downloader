from rest import Rest
from scraper import Scraper
import time

rest = Rest()
scraper = Scraper();

folderName = input("Please input the name of the folder you would like to save the images too:")
threadLink = input("Please input the link to the thread you would like:")
def run():
    threadHtml = rest.getHtml(threadLink)
    imageLinks = scraper.getImageLinks(threadHtml)

    ctr = 0
    for image in imageLinks:
        rest.downloadImage("http:"+image["imageLink"],folderName,image["imageName"])
        if ctr==5:
            time.sleep(5)
            ctr=0
    print("Downloading files into "+ folderName + " complete!")

run()