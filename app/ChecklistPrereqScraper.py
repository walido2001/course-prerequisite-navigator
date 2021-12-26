from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import PyPDF2


def extract_courses(text):
    course_list = []

    for index in range(len(text)):
        if text[index] == '/' and (text[index-5] == '_' or text[index-4] == ','):
            shortedText = text[index+1:]
            currentWord = shortedText[:shortedText.find('.')-2]
            currentWord = currentWord.replace('\n', ' ')
            if len(currentWord) == 9 and currentWord[5:].isnumeric() and currentWord[:4].isalpha() and currentWord not in course_list:
                course_list.append(currentWord)
            elif len(currentWord) == 8 and currentWord[4:].isnumeric() and currentWord[:3].isalpha():
                course_list.append(currentWord)

    return course_list


OutputFileName = ["civil", "software", "mechanical",
                  "space", "computer", "electrical"]

for courseName in OutputFileName:

    file = open("checklists/" + courseName +
                "Checklist.pdf", mode='rb')

    pyreader = PyPDF2.PdfFileReader(file)

    prereqList = []

    page_total = pyreader.getNumPages()

    for page in range(page_total):
        page_object = pyreader.getPage(page)
        page_content = page_object.extractText().replace("\n", "___")
        prereqList = prereqList + extract_courses(page_content)

    for course in prereqList:
        course = course.replace("\n", "")

    with open("EngCrs/" + courseName + "Check.json", 'w') as json_file:
        json.dump(prereqList, json_file)
