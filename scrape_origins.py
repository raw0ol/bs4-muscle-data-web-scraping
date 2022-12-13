#!/usr/bin/env python3

"""
This script uses the Beautiful Soup module (bs4) to scrape information about muscles from a website.

The script makes use of the requests module to fetch the HTML content of the website, and then uses
the bs4 module to parse the HTML and extract the relevant information.
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint

# Use the .text attribute to access the response body as a string
source = requests.get('http://www.med.umich.edu/lrc/anatomy-tables/muscles_alpha.html').text

mmRegions = ['back', 'upper limb', 'head & neck', 'thoracic', 'abdominal region', 'pelvis & perineum', 'lower limb']
mmTableHeadings = ['Muscle', 'Origin', 'Insertion', 'Action', 'Innervation', 'Artery', 'Notes']

# Use Beautiful Soup to find all td elements on the page
soup = BeautifulSoup(source, 'lxml').find_all('td')

def remove_carriage_return_and_newline(string):
    # Use the replace() method to replace \r and \n with empty strings
    return string.replace("\r", "").replace("\n", "")

allMusclesList = []
eachMuscle = []
counter = 0

# Enumerate all 'td' values that hold muscle data
for index, value in enumerate(soup[4:2060]):
    # loop through 7 columns in each row, skips the image column
    if counter == 7:
        counter = 0
        allMusclesList.append(eachMuscle)
        eachMuscle = []
        continue
    eachMuscle.append(remove_carriage_return_and_newline(value.text.strip()))
    counter += 1

for index, value in enumerate(soup[2067:2238]):
    if counter == 7:
        counter = 0
        allMusclesList.append(eachMuscle)
        eachMuscle = []
        continue
    eachMuscle.append(remove_carriage_return_and_newline(value.text.strip()))
    counter += 1

# a dictionary that holds mmRegions and each muscle in that region
groupedMuscles = {}
# a dictoarny that holds each muscles characteristics
eachMuscleDict = {}

'''
in order to group muscles by region (regions from mmRegions list)...
prev_first_letter and current_first_letter variables were created to differentiate when 
a muscles region ended based on the alphabeticalized muscle names from the source request
"e" from "erector spinae" in the muscles of the back region
'''
prev_first_letter = 'e'
current_first_letter = 'e'
region = 0

for index, item in enumerate(allMusclesList):
    eachMuscleDict[item[0]] = [item[1], item[2], item[3], item[4], item[5], item[6]]
    current_first_letter = item[0][0]
    if current_first_letter < prev_first_letter:
        region += 1
        eachMuscleDict = {}
    prev_first_letter = current_first_letter
    groupedMuscles[mmRegions[region]] = eachMuscleDict

# prints the origin of the vastus lateralis
print(groupedMuscles['lower limb']['vastus lateralis'][0])
# prints every region, muscle in that region, and characteristics of that muscle
pprint(groupedMuscles)
# prints every muscle in a list, that containts a list of every muscles characteristics
pprint(allMusclesList)

# prints all muscles
for muscle in allMusclesList:
    print(muscle[0])

# TODO
# Save to a CSV or json file
# Run python script from the command line: 
# 0 = Origin, 1 = Insertion, 2 = Action, 3 = Innervation, 4 = Artery, 5 = Notes