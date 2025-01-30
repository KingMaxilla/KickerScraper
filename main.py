import scrapData

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
        print(scrapedcontent)




print("Session ended")