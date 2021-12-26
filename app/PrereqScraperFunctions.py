from logging import NullHandler
from os import sep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver2 = webdriver.Chrome()


def find_nth_occurrence(text, Char, n):
    """
    Function that returns the nth occurence of a character within a string

    Parameters: 
    text (string): the text containing the iterations of the character
    Char (char): char that is being looked for
    n (int): the occurence of the character

    Returns: 
    index (int): index of the char's nth occurence
    """
    n2 = 0
    for index in range(len(text)):
        if(text[index] == Char):
            n2 = n2 + 1
        if(n2 == n):
            return index
    return None


def find_occurences(text, target):
    """
    Function that will return the occurences' indices of the target in a text

    Parameters:
    text (string)
    target (string)

    Returns:
    array (int)
    """
    occurences = []
    for charI in range(len(text)):
        if text[charI] == target:
            occurences.append(charI)

    return occurences


def extract_prereqs(text):
    """
    Function that extracts the course prerequisites and corequisites

    Parameters: 
    text (string): the text containing course description

    Returns: 
    array (string): array of 2 indices, first index refers to the brief course description, second refers to the prereq list
    """
    prereqs = []
    indices = [0, 0]

    try:
        index = text.lower().index("course credit exclusion")
        indices[1] = index
    except:
        pass

    try:
        index = text.lower().index("prerequisite")
        indices[0] = index
    except:
        try:
            index = text.lower().index("corequisite")
            indices[0] = index
        except:
            pass

    if indices[0] == 0 and indices[1] != 0:
        text = text[:indices[1]]
        return [text, []]

    elif indices[0] != 0 and indices[1] == 0:
        pText = text[indices[0]:]
        slashIndices = find_occurences(pText, '/')

        for i in slashIndices:
            shortText = pText[i:]
            try:
                CNameEnd = shortText.index('.')
                course = shortText[1:CNameEnd-2].replace("\n", " ")
            except ValueError:
                CNameEnd = find_nth_occurrence(
                    shortText.replace("\n", " "), ' ', 2)
                course = shortText[1:CNameEnd]
            prereqs.append(course)

        return [text[:indices[0]], prereqs]
    elif indices[0] == 0 and indices[1] == 0:
        return [text, []]
    else:
        focusedText = text[indices[0]:indices[1]]
        text = text[:indices[1]]
        slashIndices = find_occurences(focusedText, '/')

        for i in slashIndices:
            shortText = focusedText[i:]
            try:
                CNameEnd = shortText.index('.')
                course = shortText[1:CNameEnd-2].replace("\n", " ")
            except ValueError:
                CNameEnd = find_nth_occurrence(
                    shortText.replace("\n", " "), ' ', 2)
                course = shortText[1:CNameEnd]

            prereqs.append(course)
        return [text[:indices[0]], prereqs]


def extract_info(link):
    """
    Function that extracts course info such as Course title and code, description, and
    its prerequisites

    Parameters: 
    link (string): link of the course description page

    Returns: 
    array (strings/arrays): returns an array [Course Code, Course Title, Course Description, Course Prereqs]
    """

    driver2.get(link)

    CC = ""  # Course Code
    CT = ""  # Course Title
    CD = ""  # Course Description
    CP = []  # Course Prereqs

    # Extract CC and CT
    elem = driver2.find_element_by_xpath(
        '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td[1]/h1')
    PT = elem.text  # Page Title

    CB = PT.index("   ")

    CC = PT[:CB+1]

    CCSlash = CC.index('/')
    CCDot = CC.index('.')
    CC = CC[CCSlash+1:CCDot-2]
    CT = PT[CB+3:]
    CT = CT.strip()

    # Extract Description and prereqs, PD; page description, CB; course break, CPT; course prereq text
    elem = driver2.find_element_by_xpath(
        "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/p[3]")

    PD = elem.text

    CStuff = extract_prereqs(PD)
    CD = CStuff[0]
    CP = CStuff[1]
    return [CC, CT, CD, CP]


def clean_final(courseList):
    """
    """
    for courseIndex in range(len(courseList)):
        # clean the course code
        CC = courseList[courseIndex][0]
        if '/' in CC:
            slashI = CC.index('/')
            CC = CC[slashI+1:]
        if ".00" in CC:
            creditI = CC.index(".0")
            CC = CC[:(creditI-1)]
        courseList[courseIndex][0] = CC.strip()

        # clean the prereq list
        CP = courseList[courseIndex][3]
        PrereqList = []
        for prereqI in range(len(CP)):
            if ".0" in CP[prereqI]:
                PrereqList.append(CP[prereqI])

        for prereqI in range(len(PrereqList)):
            currentPrereq = PrereqList[prereqI]
            creditI = currentPrereq.index(".0")
            if '/' in currentPrereq:
                slashI = currentPrereq.index('/')
                currentPrereq = currentPrereq[slashI+1: creditI-1].strip()
            else:
                currentPrereq = currentPrereq[:creditI-1].strip()
            PrereqList[prereqI] = currentPrereq
        courseList[courseIndex][3] = PrereqList
    return courseList


def remove_duplicates(Listo):
    """
    Remove duplicates in a list

    Parameters:
    Listo (list): list containing duplicates

    Output:
    ShortListo (list): a list similar to Listo lacking any duplicates
    """
    ShortListo = []
    for component in Listo:
        if component not in ShortListo:
            ShortListo.append(component)

    return ShortListo


def find_prereq(courseName, courseList, prereqList):
    for course in courseList:
        if course[0].strip() == courseName:
            for prereq in course[3]:
                if prereq not in prereqList:
                    prereqList.append(prereq)
                    prereqList = find_prereq(
                        prereq, courseList, prereqList)
    return prereqList
