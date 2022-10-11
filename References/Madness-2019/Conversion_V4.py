# Setup
import os
import json
import csv
from pprint import pprint

## Global Variable Definitions ##

# Array Defining The Years of Which to Store in the Master Data Json Tree
years = ["2002-03","2003-04","2004-05","2005-06","2006-07"
		,"2007-08","2008-09","2009-10","2010-11","2011-12"
		,"2012-13","2013-14","2014-15","2015-16","2016-17"
		,"2017-18","2018-19"]

# Yearly Team Names Definition
yearTeams = {}
yearTeams['2002-03'] = [] 
yearTeams['2003-04'] = []
yearTeams['2004-05'] = []
yearTeams['2005-06'] = []
yearTeams['2006-07'] = []
yearTeams['2007-08'] = []
yearTeams['2008-09'] = []
yearTeams['2009-10'] = []
yearTeams['2010-11'] = []
yearTeams['2011-12'] = []
yearTeams['2012-13'] = []
yearTeams['2013-14'] = []
yearTeams['2014-15'] = []
yearTeams['2015-16'] = []
yearTeams['2016-17'] = []
yearTeams['2017-18'] = []
yearTeams['2018-19'] = []

yearQualifiers = {}
yearQualifiers['2002-03'] = [] 
yearQualifiers['2003-04'] = []
yearQualifiers['2004-05'] = []
yearQualifiers['2005-06'] = []
yearQualifiers['2006-07'] = []
yearQualifiers['2007-08'] = []
yearQualifiers['2008-09'] = []
yearQualifiers['2009-10'] = []
yearQualifiers['2010-11'] = []
yearQualifiers['2011-12'] = []
yearQualifiers['2012-13'] = []
yearQualifiers['2013-14'] = []
yearQualifiers['2014-15'] = []
yearQualifiers['2015-16'] = []
yearQualifiers['2016-17'] = []
yearQualifiers['2017-18'] = []
yearQualifiers['2018-19'] = []

# Stats To Be Analyzed
team_stats_heading = ["G", "MP", "FG", "FGA", "FG%", "2P", 
"2PA", "2P%", "3P", "3PA", "3P%", "FT", "FTA", "FT%", "ORB",
 "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS", "PTS/G"]

# Stats For Final Output
output_team_stats = ["2P%", "3P%", "FT%", "ORB/G",
 "DRB/G", "AST/G", "STL/G", "BLK/G", "TOV/G", "PF/G"]

# /G
special_stats = ["ORB","DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF"]

output_individual_stats = ["2P%", "FT%", "PTS", "AST", "TOV"]

# File Paths
from os.path import expanduser
home = expanduser("~")
save_path = home + '/Projects/Madness_2019/'
print(save_path)

## Formatting Master Data JSON Structure ##

MasterData = {}
MasterData['year'] = {}

## Function Definitions / Declarations ##

## Data Input
def ReadData(inputFile):
	# Open JSON Data File
	statFile = open(os.path.expanduser(save_path + 'Inputs/' + inputFile))
	# teamFile = open(os.path.expanduser("~/Desktop/Programming/teamNames.json"))

	# Read Stat File in as JSON format --- 
	# REMEMBER TO PUT IN FINAL BRACKET INTO JSON FILE - If cut short
	with statFile as f:
	 	data = json.load(f)
	return data

	statFile.close()

## All Team Names Population
def NamePopulation(data):
	# Populating Team Names for their corresponding year as a key
	for i in range(len(data)):
		yearTeams[data[i]['info'][0]].append(data[i]['info'][1])

## ~~ Master JSON Definition
def MasterJSONSetup(data, numYears):

	for i in range(numYears):
		MasterData['year'][years[i]] = {}
		# Range of team names in keys

		numTeams = len(yearTeams[years[i]])
		# print numTeams;
		for k in range(len(yearTeams[years[i]])):
			MasterData['year'][years[i]][yearTeams[years[i]][k]] = {}
			# Range of number of teams in given year.
			for j in range(len(yearTeams[years[i]])):
				MasterData['year'][years[i]][yearTeams[years[i]][k]]['info'] = {}
				MasterData['year'][years[i]][yearTeams[years[i]][k]]['all_team_stats'] = {}
				MasterData['year'][years[i]][yearTeams[years[i]][k]]['all_team_per_game'] = {}
				MasterData['year'][years[i]][yearTeams[years[i]][k]]['ranking'] = 0

				# MasterData['year'][years[i]][yearTeams[years[i]][k]]['roster_heading'] = []
				# MasterData['year'][years[i]][yearTeams[years[i]][k]]['team_per_game_heading'] = []
				# MasterData['year'][years[i]][yearTeams[years[i]][k]]['team_stats_heading'] = []
				# MasterData['year'][years[i]][yearTeams[years[i]][k]]['all_roster'] = []

## ~~ Populate Rankings
def RankingPopulation(rankingFile, numYears):

		rankingFile = open(os.path.expanduser(save_path + 'Inputs/' + rankingFile),'rU')

		rank = csv.reader(rankingFile)

		for row in rank:

			for i in range(numYears):

				year = years[i]

				if row[0] != 'Teams':
					teamName = row[0]
					if row[i+1]:
						# print(row[0])
						rank = row[i+1]

						# print(MasterData['year'][years[i]]['Air Force Falcons']['ranking'])
						# print(MasterData['year'][year][teamName]['ranking'])
						if teamName in yearTeams[year]:
							MasterData['year'][year][teamName]['ranking'] = rank

						if teamName not in yearQualifiers[year]:
							yearQualifiers[year].append(teamName)

		rankingFile.close()

		# Error Checking

		# Test 0
		# print(MasterData['year']['2002-03']['Air Force Falcons']['ranking'])

		# Test 1
		# year = '2005-06'
		# print(MasterData['year'][year]["RankingInfo"])
		# print(len((MasterData['year'][year]["RankingInfo"])))

		# Test 2
		# print(MasterData['year'][years[i]]["RankingInfo"])
		# print(yearTeams)

## ~~ Master Json Population
def MasterJSONPopulation(data):

	for i in range(len(data)):
		# Populating Team Name and Stat Year
								# 2002-03 -> 	 Air Force Falcons
		info = MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['info']
		info['statYear'] = data[i]['info'][0]
		info['teamName'] = data[i]['info'][1]

		# Populating Team Stats
		for j in range(len(data[i]['team_stats_heading'])):
			# Ignoring Strange Characters in 0 index of dataset. Assigning Key/Values
			if (j > 0):
				allStats = MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['all_team_stats']
				allStats[data[i]['team_stats_heading'][j]] = data[i]['all_team_stats'][j-1]

		# Adding children to all_team_per_game for each player
		numPlayers = len(data[i]['all_team_per_game'])/(len(data[i]['team_per_game_heading'])-1)
			# Subtracting 1 to get rid of Rk
		numHeaders = len(data[i]['team_per_game_heading'])-1

		# Creating Variable for ease of use	   	2002-03	   Air Force Falcons	All_Team_Per_Game    
		allPerGame = MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['all_team_per_game']

		# Populating Stats for Ranked Team Members from Most Points to Least Points
		for j in range(numPlayers):
			allPerGame[str(j)] = {};
			for k in range(numHeaders):
				allPerGame[str(j)][data[i]['team_per_game_heading'][k+1]] = [data[i]['all_team_per_game'][(numHeaders)*j+k]];
				# Looping through all data entries by team name

def MasterJSONStatBuilder(numYears):
	for i in range(numYears):

		for j in range(len(yearQualifiers[years[i]])):

			Master = MasterData['year'][years[i]][yearQualifiers[years[i]][j]]

			for k in range(len(special_stats)):

				stat = special_stats[k]
				stat_g = special_stats[k] + '/G'

				if (Master['all_team_stats'][stat] != 'null') & (Master['all_team_stats']['G'] != 'null'):
					Master['all_team_stats'][stat_g] = (float(Master['all_team_stats'][stat]) / float(Master['all_team_stats']['G']))
				else:
					Master['all_team_stats'][stat_g] = 'FLAG'

## ~~ Master Data to Array for csv purposes
def MasterDataOutput(numYears, numOutputTeamStats, numOutputIndStats):

	# Looping through number of years to extract data from each year
	for i in range(numYears):

		# Establishing year to be looped through
		year = years[i]

		# Establishing number of teams for a given year for looping purposes
		numTeams = len(yearQualifiers[year])

		## Heading Array Creation and Population ##
		headingArray = []
		headingArray.append('Teams')

		# Team stats appended
		for j in range(numOutputTeamStats):
			headingArray.append(output_team_stats[j])

		# # Individual stats - Player 1 appended
		# for j in range(numOutputIndStats):
		# 	headingArray.append('i1-' + output_individual_stats[j])

		# # Individual stats - Player 2 appended
		# for j in range(numOutputIndStats):
		# 	headingArray.append('i2-' + output_individual_stats[j])

		# # Individual stats - Player 3 appended
		# for j in range(numOutputIndStats):
		# 	headingArray.append('i3-' + output_individual_stats[j])

		headingArray.append('Ranking')

		# Creating an array for output that holds data for each team in a given year
		MasterYearArray = [0]*(numTeams+1)

		# Adding Heading Array to Master Year Array
		MasterYearArray[0] = headingArray

		# Team Stats Array Population
		for j in range(numTeams):

			# Accessor to team name
			Master = MasterData['year'][year][yearQualifiers[year][j]]

			# Defining array for team stats
			teamArray = []

			# Populating Team Name as first item in array
			teamArray.append(Master['info']['teamName'])

			# Outputting Stats from output_team_stats array
			for k in range(numOutputTeamStats):
				teamArray.append(Master['all_team_stats'][output_team_stats[k]])

			# for k in range(numOutputIndStats):
			# 	# 0 Added because the json file has an array instead of just a single data point
			# 	teamArray.append(Master['all_team_per_game']["0"][output_individual_stats[k]][0])

			# for k in range(numOutputIndStats):
			# 	# 0 Added because the json file has an array instead of just a single data point
			# 	teamArray.append(Master['all_team_per_game']["1"][output_individual_stats[k]][0])

			# for k in range(numOutputIndStats):
			# 	# 0 Added because the json file has an array instead of just a single data point
			# 	teamArray.append(Master['all_team_per_game']["2"][output_individual_stats[k]][0])


			teamArray.append((Master['ranking']))
			MasterYearArray[j+1] = teamArray

		# outputFile = (year + '_Stats.csv')
		# filePath = '~/Desktop/Programming/Madness_2019/Outputs/'

		outputFile = (save_path + 'Outputs/' + year + '_Stats.csv')
		csvOutput(outputFile, MasterYearArray)

## Print csv file
def csvOutput(outputFile, teamArray):

	with open(outputFile,"w+") as my_csv:
	    csvWriter = csv.writer(my_csv,delimiter=',')
	    csvWriter.writerows(teamArray)

## Control Panel
def main():

	## SETUP ##

	# I/O Files
	inputFile = 'All_Stats.json'
	# outputFile = 'testArray.csv'
	# rankingFile = 'Ratings_Test1.csv'
	rankingFile = 'All_Rankings.csv'

	# Years to Test
	numYears = 17
	# numStats = len(team_stats_heading)
	numOutputTeamStats = len(output_team_stats)
	numOutputIndStats = len(output_individual_stats)

	## DATA ACQUISITION ##

	# Taking data from the input file and assigning it to 'data'
	data = ReadData(inputFile)

	# Populates all team names in system for every year
	NamePopulation(data)

	## DATA POPULATION ##

	# Assigns necessary children to JSON tree
	MasterJSONSetup(data,numYears)

	# Adding RankingInfo child on MasterData
	RankingPopulation(rankingFile, numYears)

	# Populates the Master JSON file
	MasterJSONPopulation(data)

	## DATA MANIPULATION ##

	# Adds Special Stats (AST/G, BLK/G, ...)
	MasterJSONStatBuilder(numYears)

	# Master Data to Array for csv purposes
	MasterDataOutput(numYears, numOutputTeamStats, numOutputIndStats)

	## DATA OUTPUT ##

	# with open('JSON1.txt','w') as outFile:
	# 	json.dump(MasterData, outFile)

main()

## OUTPUT TESTING

	# pprint(MasterData)
	# pprint(data)
	# print(info)
	# print(MasterData['year']['2002-03']['Air Force Falcons']['all_team_per_game']["0"]["PTS"])
	# pprint(MasterData['year']['2002-03']['Air Force Falcons']['all_team_per_game'])
	# print(MasterData['year']['2002-03']['Air Force Falcons']['info']['statYear'])
	# print(MasterData['year']['2002-03']['Air Force Falcons']['all_team_stats'])
	# print(MasterData['year']['2002-03']['Air Force Falcons']['all_team_stats']['PTS'])

## DATA MANIPULATION

	# pprint(data)

	# print(data[0]["info"])

	# print(len(data))

## USER INTERFACE

	# var = raw_input("Please enter something: ")
	# print("You entered " + str(var))

	# age = raw_input("What is your age? ")
	# print "Your age is: ", age
	# type(age)

	## END OF USER INTERFACE


	## DATA WRITING

	# DATA ARRAYS

	# Gather Data For All Teams: All Years - Any Stat
	# for i in range(len(years)):
	# 	for j in range(len(yearTeams[years[i]])):
	# 		print(MasterData['year'][years[i]][yearTeams[years[i]][j]]['all_team_per_game']["0"]["PTS"])

	# Gather Data For One Team - All Years - Any Stat
	# for i in range(len(years)):
	# 	print(MasterData['year'][years[i]]['Air Force Falcons']['all_team_per_game']["0"]["PTS"])

## FOR REFERENCE
	
	# Multi-Dimensional Array for Team Stats: +1 for Team Name in i-dir, +1 for Stat Names in j-dir
	# teamteamArray = [[0]*(len(team_stats_heading)+1) for j in range(len(yearQualifiers[year])+1)]
	# Function to write team names to file
	# teamNamesArray = []
	# for i in range(len(yearTeams['2002-03'])):
	# 	teamNamesArray.append(yearTeams['2002-03'][i])

	# with open("nameArray.csv", "w") as output:
	#     writer = csv.writer(output, lineterminator='\n')
	#     for val in teamNamesArray:
	#         writer.writerow([val])

	# Reference Material
	# for j in range(numHeaders-1):

			# Team -> All_Team_Per_game -> 
			# allPerGame[data[i]['all_team_per_game'][j]]['a'] = 'b'
			# allPerGame[data[i]['all_team_per_game'][j]][data[i]['team_per_game_heading'][j]] = data[i]['all_team_per_game'][j]

		# Appending Arrays to Header Values for further addition
		# for j in range(len(data[i]['team_per_game_heading'])-1):
		# 	# Ignoring Rank on Team because it is a th text
		# 	if (j > 0):
		# 		#										2002-03			Air Force Falcons
		# 		allPerGame = MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['all_team_per_game'][0]
		# 		allPerGame[data[i]['team_per_game_heading'][j]] = []

		# for k in range(numPlayers):
		# 	for j in range(len(data[i]['team_per_game_heading'])):
		# 	# Ignoring Rank on Team because it is a th text
		# 		if (j > 0):
		# 			#										2002-03			Air Force Falcons
		# 			allPerGame = MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['all_team_per_game']
		# 			allPerGame[data[i]['team_per_game_heading'][j]].append(data[i]['all_team_per_game'][k])


		# MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['roster_heading'] = data[i]['roster_heading']
		# MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['team_per_game_heading'] = data[i]['team_per_game_heading']
		# MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['all_team_per_game'] = data[i]['all_team_per_game']
		# MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['team_stats_heading'] = data[i]['team_stats_heading']
		#
		#	IMPORTANT STATS HERE
		# MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['all_roster'] = data[i]['all_roster'] --- TACKLING THIS ONE NEXT
		#
		#
		# Populating All Team Stats

	# print(MasterData['year']['2002-03']['Air Force Falcons']['info']['statYear'])
	# print(MasterData['year']['2002-03']['Air Force Falcons']['all_team_stats'])
	# print(MasterData['year']['2002-03']['Air Force Falcons']['all_team_stats']['PTS'])

	# print(MasterData['year']['2002-03']['Air Force Falcons']['all_team_per_game'])

	# print(data[0]['all_team_per_game'])
	# print(data[0]['team_per_game_heading'])
	# print(len(data[0]['all_team_per_game']))
	# print(len(data[0]['team_per_game_heading'])-1)
	# print(MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['all_team_per_game'])

	# for p in MasterData['year']['2002-03']['Air Force Falcons']['all_team_stats']:
	# 	print(p['MP'])


	# info = []
	# info = (data[0]["info"][0])

	# year = (data[0]["info"][0])
	# team = (data[0]["info"][1])


	# team_stats_heading_len = len(data[0]["team_stats_heading"])

	# for i in range(team_stats_heading_len):
	# 	MasterData['year'][data[0]["info"][0]][data[0]["info"][1]]["all_team_stats"].append({
	# 		'a':'words'
	# 		# data[0]["team_stats_heading"][i] : data[0]["all_team_stats"][i]
	# 	})

	# MasterData -> 	2002-2003 ->		Air Force Falcons -> 
	# MasterData['year'][data[0]["info"][0]][data[0]["info"][1]]["all_team_stats"].append({

	# 	})


	# str(year)
	# str(team)

	# MasterData['year'][year]['all_team_stats'].append({
	# 	'a':'hello'
	# 	})
	# MasterData['year'][0].append(team)
	# MasterData['year'][0]['teams'].append(team)

		# numPlayers = len(data[0]['all_team_per_game'])/(len(data[0]['team_per_game_heading'])-1)
		# for j in range(len(data[i]['team_per_game_heading'])):
		# 	# Ignoring Rank on Team because it is a th text
		# 	if (j > 0):
		# 		#										2002-03			Air Force Falcons
		# 		allPerGame = MasterData['year'][data[i]['info'][0]][data[i]['info'][1]]['all_team_per_game']
		# 		allPerGame[data[i]['team_per_game_heading'][j]] = data[i]['all_team_per_game'][j-1]

	# More Reference
		# # Populating Team Members into Json
		# for j in range(len(data[i]['all_team_per_game'])):
		# 	if (j % (numHeaders-1) == 0):
	 
		# 		# Creating JSON cabability for each individual player
		# 		allPerGame[data[i]['all_team_per_game'][j]] = {}

		# 		# This is the working entry protocol for the team members #
		# 		# allPerGame[data[i]['all_team_per_game'][j]]['a'] = 'b'
		
		# 		# Populating Individual Stats to Each Player
		# 		for k in range(numHeaders):

		# 			# Stats lined up with corressponding headers
		# 			# allPerGame[data[i]['all_team_per_game'][j]][data[i]['team_per_game_heading'][k]] = [data[i]['all_team_per_game'][k+j-1]]

		# 			allPerGame[data[i]['all_team_per_game'][j]][data[i]['team_per_game_heading'][k]] = [data[i]['all_team_per_game'][k+j-1]]

