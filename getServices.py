import functions, codecs

#Server Information - specify the REST endpoint and desired URL protocol ("SOAP" or "REST")
restURL = "http://sampleserver6.arcgisonline.com/arcgis/rest/services"
protocol = "REST"

#If you wish to use a token, set getToken to true and specify following parameters
getToken = False
tokenURL = "http://sampleserver6.arcgisonline.com/arcgis/tokens/generateToken"
username = "user1"
password = "user1"

#Get Token and Service List from Server
if getToken == True:
    token = functions.getToken(tokenURL, username, password)['token']
    serviceList = functions.restCrawl(restURL, token, protocol)
else:
    serviceList = functions.restCrawl(restURL, "", protocol)

#Write service list to text file
log = codecs.open("services.txt",encoding='utf-8', mode="w+")
for service in serviceList:
    print service
    log.write(service + "\n")
log.close()
