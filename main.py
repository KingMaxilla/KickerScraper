import scrapData
import format
import formatNames
import createJSON

print("Session started")

#read links
links = []
with open("links.txt", "r")as file:
    for line in file:
        links.append(line)

        #scrap content
        scrapedcontent = []
        for i in range(len(links)):
            scrapedcontent = scrapData.scrap(link=links[i])
        
        #format content
        formattedcontent = format.formatOutput(listOutput=scrapedcontent)
        formattedcontent = formatNames.formatAgain(formatedData=formattedcontent)
        
        #conevert to JSON
        for i in range(len(formattedcontent)):
            print(formattedcontent[i])




print("Session ended")