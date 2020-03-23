from bs4 import BeautifulSoup

class Scraper:

    def getImageLinks(self,html):
        soup = BeautifulSoup(html,"html.parser")
        images = soup.body.find_all("a",class_="fileThumb")
        imageLinks = []
        for img in images:
            imgLink = img.attrs["href"]
            temp = imgLink.split("/")
            imgName= temp[len(temp)-1]
            imageLinks.append({"imageLink":imgLink,"imageName":imgName})
        return imageLinks