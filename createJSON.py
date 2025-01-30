import json

def createJSON(originalNameLeague, convertedDataTeams):
    try:
        jsonFile = open("data.json", "x")
        print("JSON created")
    except:
        pass
    
    with open("data.json", "w") as jsonFile:
        data = {
            originalNameLeague : {

            }
        }
        for i in range(len(convertedDataTeams)):
            data[convertedDataTeams[i][2]] = {
                "Position": convertedDataTeams[i][0],
                "Played": convertedDataTeams[i][3],
                "Won": convertedDataTeams[i][4],
                "Drawn": convertedDataTeams[i][5],
                "Lost": convertedDataTeams[i][6],
                "Goals": convertedDataTeams[i][7],
                "GoalsFor": convertedDataTeams[i][8],
                "GoalsAgainst": convertedDataTeams[i][9],
            }
            
         