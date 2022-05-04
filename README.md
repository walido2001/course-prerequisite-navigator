# Course Prerequisite Navigator
A webapp developed using Flask (python back-end) and designed with bootstrap (CSS framework), aimed at students. The webapp helps students quickly 
determine course prerequisites with a click of a button, as well as see the route of courses needed to be taken in order to enroll in the clicked course.

## Visual Demonstration
Assume a 3rd year student enrolled in software engineering would like to determine what the prerequisites for "EECS 3216". 
<img width="1436" alt="Screen Shot 2022-04-22 at 3 31 22 PM" src="https://user-images.githubusercontent.com/78936295/164781968-f6648104-e3fd-4ba3-ab6a-bbf75dd19fc6.png">

Upon clicking on the course button "EECS 3216". All the prerequisites for that course will light up, as well as the course description for the clicked course. 
The prerequisites that appear also include indirect prerequisites, meaning the prerequisites of the prerequisites.
<img width="1432" alt="Screen Shot 2022-04-22 at 3 34 09 PM" src="https://user-images.githubusercontent.com/78936295/164782237-af64bace-7df5-450e-b52b-008de32d34de.png">

## How It Works
  -> Course data for every engineering major is webscraped off the official YorkU course website (https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm) <br />
  -> Python scripts filter and clean up the data <br />
  -> Data is stored into JSON files <br />
  -> JSON files are read by Flask (the backend framework for the webapp) and course data is extracted accordingly <br />
 
## Issues
  -> The python scripts that webscrape and clean up the data are run manually, meaning course data isn't always up-to-date with the official course website <br />
  -> Official Yorku course website sometimes contains outdated info about courses, which in turn messes with the webapp <br />
  
## Improvements Needed
  -> Creation of an API that regularly runs the python scripts that extract data from the official course website and cleans it up
  -> Elimination of outdated info through manual checks
