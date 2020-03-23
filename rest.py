from urllib import request
import os

class Rest:
    def __init__(self):
        self.user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"

    def getHtml(self,url):
        newRequest = request.Request(url,headers={"user-agent":self.user_agent})
        htmlToReturn = request.urlopen(newRequest).read()
        return htmlToReturn

    def downloadImage(self, url, filePath, fileName):
        if os.path.exists(filePath)==False:
            os.mkdir(filePath)
        retrieveRequest = request.Request(url,headers={"user-agent":self.user_agent})
        imageToWrite = request.urlopen(retrieveRequest).read()
        file = open(filePath+"\\"+fileName, "wb")
        file.write(imageToWrite)
        file.close()
