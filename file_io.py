players = []

with open("team.csv", "r") as file:
    for line in file:
        firstname, lastname, position = line.strip().split(",")
        player = {"firstname":firstname, "lastname":lastname, "position":position}
        players.append(player)

for player in sorted(players, key=lambda player: (player['lastname'], player['position'])):    
        print(f"{player['firstname']} {player['lastname']} - {player['position']}")
        
with open("sorted_team.csv", "w") as file:
    for player in sorted(players, key=lambda player: (player['lastname'], player['position'])):
        file.write(f"{player['firstname']},{player['lastname'],{player['position']}}\n")