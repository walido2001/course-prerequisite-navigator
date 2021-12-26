from os import remove
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import PrereqScraperFunctions
import PyPDF2

CsInfo = []
driver = webdriver.Chrome()

CivilEng = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[4]/select/option[1]"
EECSEng = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[4]/select/option[3]"
ENGEng = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[4]/select/option[4]"
ESSEEng = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[4]/select/option[5]"
MECHEng = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[4]/select/option[6]"

CHEMScience = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[4]/select/option[5]"
MATHScience = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[4]/select/option[9]"
PHYSScience = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[4]/select/option[12]"

EngFaculty = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/select/option[8]"
ScienceFaculty = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/select/option[11]"

runThroughList = [[EngFaculty, CivilEng, "CIVIL"], [EngFaculty, EECSEng, "EECS"], [
    EngFaculty, ENGEng, "ENG"], [EngFaculty, ESSEEng, "ESSE"], [EngFaculty, MECHEng, "MECH"], [ScienceFaculty, CHEMScience, "CHEM"],
    [ScienceFaculty, MATHScience, "MATH"], [ScienceFaculty, PHYSScience, "PHYS"]]

for major in runThroughList:

    driver.get(
        'https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm')

    time.sleep(0.5)

    #MAIN PAGE#############################################################
    # Access main page and click on "Advanced Search"
    elem = driver.find_element_by_xpath(
        "/html/body/p/table/tbody/tr[2]/td[1]/table/tbody/tr[12]/td/a/img")
    elem.click()

    #ADVANCED SEARCH PAGE###################################################
    # Select the correct filters, starting with faculty, then Subject then, Session

    # Click on "Lassonde school of engineering" in the Faculty section
    elem = driver.find_element_by_xpath(major[0])
    elem.click()

    time.sleep(0.5)

    # Click on "X Engineering" in the Subject section
    elem = driver.find_element_by_xpath(major[1])
    elem.click()

    # click on "Fall/Winter" in the Session section
    elem = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[4]/td[2]/select/option[2]")
    elem.click()

    # click on "Search Courses"
    elem = driver.find_element_by_xpath(
        '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/input')
    elem.click()

    time.sleep(0.5)

    #ENG COURSE LIST######################################################
    # CL = Course Links, extract the links of the list of courses, and then visit each site
    # and extract the required info

    elem = driver.find_elements_by_link_text(
        'Fall/Winter 2021-2022 Course Schedule')

    CLI = [link.get_attribute('href') for link in elem]

    CsInfo = [PrereqScraperFunctions.extract_info(link) for link in CLI]

    with open("CourseData/" + major[2] + "CourseData.json", 'w') as json_file:
        json.dump(CsInfo, json_file)
    CsInfo = []


driver.close()
PrereqScraperFunctions.driver2.close()
# visit each link and extract the course code, name, and prereqs
