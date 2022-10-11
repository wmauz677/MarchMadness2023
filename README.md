<div align=center>

  [![MIT License][license-shield]][license-url]
  ![Language][language-shield]

</div>

<!-- PROJECT LOGO -->

<br />
<p align="center">
  <a href="https://wmauz677.github.io/East-Meets-Weast/">
    <img src="Images/logo.jpeg" alt="Logo" width="200" height="100">
  </a>

  <h3 align="center">March Madness 2023</h3>
  <h3 align="center">Creator: Weston Mauz</h3>
  <h3 align="center">Project Start: September 28, 2022</h3>
</p>

---

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

# 1. Problem Statement

The purpose of this project is to produce a model to predict the winners of the 2023 March Madness college basketball tournament. 

#### Key Points:

- All data will be acquired through Beautiful Soup from: https://www.sports-reference.com/cbb/
- The programming will be done inside of jupyter notebooks
- The data will be modified & analyzed using Python w/ the Pandas package
- This project will help to practice newly acquired data science skills

#### Built With:
Code Editor
* [VSCode](https://code.visualstudio.com)
<img src="Images/vs-code-icon.png" alt="Logo" width="128" height="128">

Developer Platform
* [GitHub](https://github.com/wmauz677)

Terminal
* [iTerm2](https://iterm2.com)

Operating System
* [MacOS](https://www.apple.com/macos/monterey/)

Data Visualization
* [Numbers](https://www.apple.com/numbers/)



# 2. Data Extraction

**Statement:** The data extraction for the project is performed inside of two separate files.

The first file 'dataExploration.ipynb' is intended to only be run once, as it establishes the foundation for the project. The file does the following:

- All team names on the webpage, then writes them to 'Data/team_names.csv'
- Assign Team IDs based on alphabetical index (ex. 0,1,2)
- Collects the links to each team home page (ex. colorado/, colorado-state/)
- Collects the links to each year for each team where statistics exist (ex. 2021, 2022)
- References 'Team' Object (see here -- **insert link**)
- Creates & writes data to 'teams_dictionary' which is a [key:value] of [team_name:Team] and acts as the main data dictionary in this project. 
- Locates, Collects, Formats, Writes all stat labels to be collected (ex. mp_per_g, fg_per_g). They are written to: 'Data/stat_labels.csv'

The second file 'dataAcquisition.ipynb' can be run multiple times in different configurations depending on the data the user would like to collect. The file performs the following actions:

- Extracts & Formats team data for a given year
- Assigns year data to main 'teams_dictionary' & writes 'teams_dictionary' to pkl file: Data/teams_dictionary.pkl
- Retrieve March Madness Results from csv & translate to result_dictionary with [key:value] of [team_name][rankings_dictionary] where 'rankings_dictionary' is composed of [year:result]
- Write March Madness Results dictionary to 'result_dictionary.pkl'
- Reads 'result_dictionary.pkl'
- Compiles dataframe with all team stats + march madness results for a given year. Writes this dataframe to: 'Data/Madness/{year}.csv'

# 3. Exploratory Data Analysis


# 9. Acknowledgements

### Note: The crawling of College Basketball Team data is not prohibited by SportsReference.com

Data Source
* [Sports Reference](https://www.sports-reference.com/cbb/)
* [Sports Reference Robots.txt](https://www.sports-reference.com/robots.txt)

<img src="Images/robots-text.png" alt="Logo" width="384" height="512">

# 10. License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- MARKDOWN LINKS & IMAGES -->

[language-shield]: https://img.shields.io/github/languages/top/wmauz677/MarchMadness2023?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/wmauz677/marchmadness2023?style=for-the-badge
[license-url]: https://github.com/wmauz677/personalWeb/blob/gh-pages/LICENSE
[project-screenshot]: Images/project-screenshot.png