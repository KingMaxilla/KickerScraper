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
    for i in range(len(links)):
            
        scrapedcontent = []
        scrapedcontent = scrapData.scrap(link=links[i])
            
        #format content
        formattedcontent = format.formatOutput(listOutput=scrapedcontent)
        formattedcontent = formatNames.formatAgain(formatedData=formattedcontent)
            
        #convert to JSON
        createJSON.createJSON(originalNameLeague=scrapedcontent[0][0], convertedDataTeams=formattedcontent)




print("Session ended")