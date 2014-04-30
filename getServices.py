import functions, codecs

#Server Information
tokenURL = "http://sampleserver6.arcgisonline.com/arcgis/tokens/generateToken"
restURL = "http://sampleserver6.arcgisonline.com/arcgis/rest/services"
username = "user1"
password = "user1"

#Get Token and Service List from Server
token = functions.getToken(tokenURL, username, password)['token']
serviceList = functions.restCrawl(restURL, token, "SOAP")

#Write service list to text file
log = codecs.open("services.txt",encoding='utf-8', mode="w+")
for service in serviceList:
    print service
    log.write(service + "\n")
log.close()
