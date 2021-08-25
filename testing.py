import json
import PrereqScraperFunctions

jfile = open("EngCrs/civilFINAL.json")
courseList = json.load(jfile)

with open('EngCrs/civilFINALTEST.json', 'w') as json_file:
    json.dump(PrereqScraperFunctions.clean_final(courseList), json_file)
