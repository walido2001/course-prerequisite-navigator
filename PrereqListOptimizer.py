import json
import PrereqScraperFunctions

Engnames = ["CIVIL", "EECS", "ENG", "MECH"]
Extranames = ["CHEM", "MATH", "PHYS", "ESSE", "ENG"]
ExtraCourseList = []

for name in Extranames:
    jfile = open("CourseData/" + name + "CourseData.json")
    ExtraCourseList = ExtraCourseList + json.load(jfile)


for name in Engnames:
    jfile = open("CourseData/" + name + "CourseData.json")
    major = json.load(jfile) + ExtraCourseList

    majorTitles = [course[0] for course in major]

    for courseI in range(len(major)):
        major[courseI][3] = PrereqScraperFunctions.find_prereq(
            major[courseI][0], major, [])

        prereqList = []
        for prereq in major[courseI][3]:
            if prereq in majorTitles:
                prereqList.append(prereq)
        major[courseI][3] = prereqList
        prereqList = []

    with open("CourseDataOptimized/" + name + "OpCourseData.json", 'w') as json_file:
        json.dump(major, json_file)


with open("CourseDataOptimized/ESSEOpCourseData.json", 'w') as json_file:
    json.dump(ExtraCourseList, json_file)
