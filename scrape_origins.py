import requests
from bs4 import BeautifulSoup
from pprint import pprint


source = requests.get('http://www.med.umich.edu/lrc/anatomy-tables/muscles_alpha.html').text

mmRegions = ['back', 'upper limb', 'head & neck', 'thoracic', 'abdominal region', 'pelvis & perineum', 'lower limb']
mmTableHeadings = ['Muscle', 'Origin', 'Insertion', 'Action', 'Innervation', 'Artery', 'Notes']

# # finds mmTableHeadings
# soup = BeautifulSoup(source, 'lxml').find_all('th')
# for index, value in enumerate(soup):
#     if index % 9 == 0 or value.text == 'Image':
#         continue
#     elif value.text not in mmTableHeadings:
#         mmTableHeadings.append(value.text)

allMusclesList = []
eachMuscle = []
soup = BeautifulSoup(source, 'lxml').find_all('td')

counter = 0
for index, value in enumerate(soup[4:2060]): #2056 fover every value here...
    if counter == 7:
        counter = 0
        allMusclesList.append(eachMuscle)
        eachMuscle = []
        continue 
    eachMuscle.append(value.text.strip())
    counter += 1

for index, value in enumerate(soup[2067:2238]):
    if counter == 7:
        counter = 0
        allMusclesList.append(eachMuscle)
        eachMuscle = []
        continue
    eachMuscle.append(value.text.strip())
    counter += 1


groupedMuscles = {}
eachMuscle = {}

previousLetter = 'e'
firstLetter = 'e'
region = 0
for index, item in enumerate(allMusclesList):
    eachMuscle[item[0]] = [item[1], item[2], item[3], item[4], item[5], item[6]]
    firstLetter = item[0][0]
    if firstLetter < previousLetter:
        region += 1
        eachMuscle = {}
    previousLetter = firstLetter
    groupedMuscles[mmRegions[region]] = eachMuscle

pprint(groupedMuscles['lower limb']['vastus lateralis'][0])

## list of all muscles
# for muscle in allMusclesList:
#     print(muscle[0])

#TODO Convert to json

#TODO Remove \r\n from strings
# Pseudo Code
# if current stirng index iis == empty string:
#     then next string index should not be ''
#     if current string is '' and next four strings == '\r\n':
#         delete until current string is empty and next string has a letter or number or. 