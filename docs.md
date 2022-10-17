# Documentation

Project Name: March Madness 2023
Creator: Weston Mauz
Project Start: September 28, 2022

### Project Index:

1. [Problem Statement](#1-Problem-Statement)

2. [Data extraction](#2-Data-Extraction)

3. Exploratory Data Analysis

4. Feature Engineering

5. Feature Selection

6. Model Selection

7. Model tuning

8. Model serving (if applicable)

9. [Acknowledgements](#9-Acknowledgements)

10. [License](#10-License)

## 1. Problem Statement

The purpose of this project is to produce a model to predict the winners of the 2023 March Madness college basketball tournament. 

#### Key Points:

- All data will be acquired through Beautiful Soup from: https://www.sports-reference.com/cbb/
- The programming will be done inside of jupyter notebooks
- The data will be modified & analyzed using Python w/ the Pandas package

## 2. Data Extraction

### **Files:**

#### Data Exploration
*'00-data-exploration.ipynb'*

This file is intended to be run once (and only once) to establish the data foundation for the project. 

**The file performs the following:**

- Gathers all NCAA Basketball team names on the webpage, then writes them to 'Data/team_names.csv'
- Assigns Team IDs based on alphabetical index (ex. 0,1,2)
- Collects the links to each team home page (ex. colorado/, colorado-state/)
- Collects the links to each year for each team where statistics exist (ex. 2021, 2022)
- References 'Team' class. See here: https://github.com/wmauz677/MarchMadness2023/blob/main/Classes/team.py
- Creates & writes data to 'teams_dictionary' which is a [key:value] of [team_name:Team] and acts as the main data dictionary in this project. 
- Locates, Collects, Formats, Writes all stat labels to be collected (ex. mp_per_g, fg_per_g). They are written to: 'Data/stat_labels.csv'
- Writes Teams Dictionary to 'Data/teams_dictionary.pkl'

#### Data Acquisition
*'01-data-acquisition.ipynb'*

This can be run multiple times in different configurations depending on the data the user would like to collect. The file performs the following actions:

**The file performs the following:**

- Extracts & Formats team data for a given year
- Assigns year data to main 'teams_dictionary' & writes 'teams_dictionary' to pkl file: Data/teams_dictionary.pkl
- Retrieve March Madness Results from csv & translate to result_dictionary with [key:value] of [team_name][rankings_dictionary] where 'rankings_dictionary' is composed of [year:result]
- Write March Madness Results dictionary to 'result_dictionary.pkl'
- Reads 'result_dictionary.pkl'
- Compiles dataframe with all team stats + march madness results for a given year. Writes this dataframe to: 'Data/Madness/{year}.csv'


## 3. Exploratory Data Analysis

### **Files:**

#### Data Composition
*'data-composition.ipynb'*

Compiles data for use in the exploratory data analysis.

**The file performs the following:**

- Updates teams_dictionary with data_dictionary files for given years in 'Data/Yearly/{year}_data_dictionary.pkl'
- Reads 'Data/Results/madness_results_confirmed.csv' & translates into dictionary, then writes to 'Data/Results/results_dictionary.pkl' for later access
- Compiles March Madness dataframes from teams_dictionary and results_dictionary and writes to  'Data/Madness/{year}.csv'
- Compiles are March Madness year dataframes into one larger dataframe and writes to 'Data/Madness/all_years.csv'

#### Exploratory Data Analysis
*'02-exploratory-data-anlysis.ipynb'*

## 4. Feature Engineering

### **Files:**

#### Feature Engineering
*'03-feature-engineering.ipynb'*

## 5. Feature Selection

### **Files:**