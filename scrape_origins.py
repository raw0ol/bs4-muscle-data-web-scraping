import requests
from bs4 import BeautifulSoup
from pprint import pprint


source = requests.get('http://www.med.umich.edu/lrc/anatomy-tables/muscles_alpha.html').text

# jsonDummyMM = {'LE' : {'Quad' : ['origin', 'insertion', 'description'],
#                         'Hamstring': ['origin', 'insertion', 'description'],
#                         'Calf': ['origin', 'insertion', 'description']},
#             'UE' : {'Quad' : ['quad origin', 'quad insertion', ' quad description'],
#                         'Hamstring': ['ham origin', 'ham insertion', 'ham description'],
#                         'Calf': ['calf origin', 'calf insertion', 'calf description']}

# }

# print(jsonDummyMM['UE']['Quad'])

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


# for item in mmRegions:
#     mmDict[item] = None

# mmDict['back'] = {'Quad' : ['origin', 'insertion', 'description']}


# print(mmDict['back']['Quad'])


mmDict = {}
newDict = {}

previousLetter = 'e'
firstLetter = 'e'
region = 0

for index, item in enumerate(allMusclesList):
    newDict[item[0]] = [item[1], item[2], item[3], item[4], item[5], item[6]]
    firstLetter = item[0][0]
    if firstLetter < previousLetter:
        region += 1
        newDict = {}
    previousLetter = firstLetter
    mmDict[mmRegions[region]] = newDict

pprint(mmDict['back']['erector spinae'][0])
    
#TODO Convert to json

# for muscle in allMusclesList:
#     print(muscle[0])




# -------------------------------------------------------------------------------------------------------
# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint


# source = requests.get('http://www.med.umich.edu/lrc/anatomy-tables/muscles_alpha.html').text

# # jsonDummyMM = {'LE' : {'Quad' : ['origin', 'insertion', 'description'],
# #                         'Hamstring': ['origin', 'insertion', 'description'],
# #                         'Calf': ['origin', 'insertion', 'description']},
# #             'UE' : {'Quad' : ['quad origin', 'quad insertion', ' quad description'],
# #                         'Hamstring': ['ham origin', 'ham insertion', 'ham description'],
# #                         'Calf': ['calf origin', 'calf insertion', 'calf description']}

# # }

# # print(jsonDummyMM['UE']['Quad'])

# mmRegions = ['back', 'upper limb', 'head & neck', 'thoracic', 'abdominal region', 'pelvis & perineum', 'lower limb']
# mmTableHeadings = ['Muscle', 'Origin', 'Insertion', 'Action', 'Innervation', 'Artery', 'Notes']

# # # finds mmTableHeadings
# # soup = BeautifulSoup(source, 'lxml').find_all('th')
# # for index, value in enumerate(soup):
# #     if index % 9 == 0 or value.text == 'Image':
# #         continue
# #     elif value.text not in mmTableHeadings:
# #         mmTableHeadings.append(value.text)

# allMusclesList = []
# eachMuscle = []
# soup = BeautifulSoup(source, 'lxml').find_all('td')

# counter = 0
# for index, value in enumerate(soup[4:2060]): #2056 fover every value here...
#     if counter == 7:
#         counter = 0
#         allMusclesList.append(eachMuscle)
#         eachMuscle = []
#         continue
#     eachMuscle.append(value.text.strip())
#     counter += 1

# for index, value in enumerate(soup[2067:2238]):
#     if counter == 7:
#         counter = 0
#         allMusclesList.append(eachMuscle)
#         eachMuscle = []
#         continue
#     eachMuscle.append(value.text.strip())
#     counter += 1


# # for item in mmRegions:
# #     mmDict[item] = None

# # mmDict['back'] = {'Quad' : ['origin', 'insertion', 'description']}


# # print(mmDict['back']['Quad'])


# mmDict = {}
# newDict = {}

# fistLetter = 'e'
# region = 1

# if first letter is equal to veryFirstLetter:
#     change region
#     veryFirstLetter = first letter

# for region in enumerate(mmRegions):
#     for index, item in enumerate(allMusclesList):
#         newDict[f'{item[0]}'] = [item[1], item[2], item[3], item[4], item[5], item[6]]
#     mmDict[region] = newDict
#     newDict = {}


# pprint(mmDict)
    