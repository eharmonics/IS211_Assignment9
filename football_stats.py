from re import S
from bs4 import BeautifulSoup
import requests
import numpy as np
count = 0

URL = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="TableBase-shadows")
All_Players = soup.find_all("tr", class_="TableBase-bodyTr")

output = ""
for player in All_Players:
    if count == 20:
        break
    count += 1
    player_name = player.contents[0].contents[1].contents[0].a.getText()
    player_position = player.contents[0].contents[0].contents[0].contents[1].text
    player_teamName = player.contents[0].contents[0].contents[0].contents[2].text
    gamesplayed = player.contents[1].getText()
    player_passingAttempts = player.contents[2].getText()
    player_passingCompletions = player.contents[3].getText()
    player_passingCompletionPercentage = player.contents[4].getText()
    player_passingYards = player.contents[5].getText()
    player_passingYardsPerGame = player.contents[6].getText()
    player_longestCompletion = player.contents[7].getText()
    player_touchDownPasses = player.contents[8].getText()
    player_interceptions = player.contents[9].getText()
    player_timesSlacked = player.contents[10].getText()
    player_slacksYardsLost = player.contents[11].getText()
    player_passerRating = player.contents[12].getText()
    output = output + player_name.strip() + "\t\t" + player_position.strip() + "\t\t\t" + player_teamName.strip() + "\t\t" + player_touchDownPasses.strip() + "\t\t" + player_passerRating.strip() + "\n" 

print("============================================================================================")
print("Name\t\t\tPosition\t\tTeam\t\tTD\t\tRate")
print("============================================================================================")

print(output)
