**Note:** The data extraction for the project is performed inside of two separate files: 'dataExploration.ipynb' & 'dataAcquisition.ipynb' 

00 Data Exploration
'00-data-exploration.ipynb'

**The file performs the following**:

- Gathers all NCAA Basketball team names on the webpage, then writes them to 'Data/team_names.csv'
- Assigns Team IDs based on alphabetical index (ex. 0,1,2)
- Collects the links to each team home page (ex. colorado/, colorado-state/)
- Collects the links to each year for each team where statistics exist (ex. 2021, 2022)
- References 'Team' class. See here: https://github.com/wmauz677/MarchMadness2023/blob/main/Classes/team.py
- Creates & writes data to 'teams_dictionary' which is a [key:value] of [team_name:Team] and acts as the main data dictionary in this project. 
- Locates, Collects, Formats, Writes all stat labels to be collected (ex. mp_per_g, fg_per_g). They are written to: 'Data/stat_labels.csv'
- Writes Teams Dictionary to 'Data/teams_dictionary.pkl'

01 Data Exploration
'01-data-acquisition.ipynb'

 This can be run multiple times in different configurations depending on the data the user would like to collect. The file performs the following actions:

- Extracts & Formats team data for a given year
- Assigns year data to main 'teams_dictionary' & writes 'teams_dictionary' to pkl file: Data/teams_dictionary.pkl
- Retrieve March Madness Results from csv & translate to result_dictionary with [key:value] of [team_name][rankings_dictionary] where 'rankings_dictionary' is composed of [year:result]
- Write March Madness Results dictionary to 'result_dictionary.pkl'
- Reads 'result_dictionary.pkl'
- Compiles dataframe with all team stats + march madness results for a given year. Writes this dataframe to: 'Data/Madness/{year}.csv'

02 Exploratory Data Analysis
'02-exploratory-data-anlysis.ipynb'

