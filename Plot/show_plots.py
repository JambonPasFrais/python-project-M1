import os
import player_plot
import matplotlib.pyplot as plt
import team_plot

#get the list of all the files in the players_stats directory
players_list = os.listdir("../Scrapping/players_stats")
players_list.sort()
print("Choose the player :")
#Remove .csv extension and print the name of the player
for i in range(len(players_list)):
    players_list[i] = players_list[i].replace('.csv','')
    print(str(i+1)+". "+players_list[i])

#MARIE - players_list : liste de tous les joueurs qui ont été scraps
try:
    choice = int(input("Enter your choice: "))
    if choice > len(players_list) or choice < 1:
        print("Invalid choice, try again")
    else:
        """A UTILISER PAR MARIE :)"""
        #Choice : var pour le nom du player (Prénom Nom)
        choice = players_list[choice - 1]
        #Appeler ces fonctions
        has_played = player_plot.hasPlayed(choice)
        #Si le joueur a joué dans au moins 1 saison
        if has_played > 0:
            season = '2022-23'
            print("Generating plots...")
            player_plot.plot_all_data(choice, season)
            print("Files generated ! You can find them in the player_plot_images folder.")
        else:
            print("The player has not played yet.")
        """FIN DE L'UTILISATION PAR MARIE :)"""
except:
    print("Invalid input, try again")

"""teams_list = os.listdir("../Scrapping/teams_stats")
teams_list.sort()
print("Choose the team :")
#Remove .csv extension and print the name of the player
for i in range(len(teams_list)):
    teams_list[i] = teams_list[i].replace('.csv','')
    print(str(i+1)+". "+teams_list[i])


try:
    choice = int(input("Enter your choice: "))
    if choice > len(teams_list) or choice < 1:
        print("Invalid choice, try again")
    else:
        team_plot.plot_evolution(teams_list[choice - 1])
except:
    print("Invalid input, try again")"""
