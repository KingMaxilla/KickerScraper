def formatOutput(listOutput):
    listOutput.pop(1)
    leagueTable = []
    for i in range(1, len(listOutput)):
        clubPosition = []
        for j in range(11):
            if j == 1 or j == 2:
                continue
            else:
                clubPosition.append(listOutput[i][j])
        leagueTable.append(clubPosition)

    return leagueTable       