import json

def createJSON(originalNameLeague, convertedDataTeams):
    if '/' in originalNameLeague:
        originalNameLeague = originalNameLeague.replace('/', ' ')
    
    with open(f"data/{originalNameLeague}.json", "w") as jsonFile:
        data = {}
        for i in range(len(convertedDataTeams)):
            data[convertedDataTeams[i][1]] = {
                "Position": convertedDataTeams[i][0],
                "Played": convertedDataTeams[i][2],
                "Won": convertedDataTeams[i][3],
                "Drawn": convertedDataTeams[i][4],
                "Lost": convertedDataTeams[i][5],
                "Goals": convertedDataTeams[i][6]
            }
        json.dump(data, jsonFile, indent=4)