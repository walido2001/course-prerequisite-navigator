from types import prepare_class
from flask import Flask, redirect, url_for, render_template, request
import json
import logging
import datetime
import string
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")

# CIVIL


@app.route('/civil')
def civil_page():
    return civil_page_link(None)


@app.route('/civil/<course>')
def civil_page_link(course):

    jfile = open("app/CourseDataOptimized/CIVILOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("app/EngCrs/civilCheck.json")
    courseCheckList = json.load(jfile)
    CourseInfo = None

    try:
        course = course.replace('-', ' ')
    except AttributeError:
        course = None

    for courseSection in courseDataList:
        if courseSection[0] == course:
            CourseInfo = courseSection

    return render_template("eng.html", cList=courseCheckList, CourseData=CourseInfo, major="civil")

# Computer


@app.route('/computer')
def computer_page():
    return computer_page_link(None)


@app.route('/computer/<course>')
def computer_page_link(course):

    jfile = open("app/CourseDataOptimized/EECSOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("app/EngCrs/computerCheck.json")
    courseCheckList = json.load(jfile)
    CourseInfo = None

    try:
        course = course.replace('-', ' ')
    except AttributeError:
        course = None

    for courseSection in courseDataList:
        if courseSection[0] == course:
            CourseInfo = courseSection

    return render_template("eng.html", cList=courseCheckList, CourseData=CourseInfo, major="computer")

# Software


@app.route('/software')
def software_page():
    return software_page_link(None)


@app.route('/software/<course>')
def software_page_link(course):

    jfile = open("app/CourseDataOptimized/EECSOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("app/EngCrs/softwareCheck.json")
    courseCheckList = json.load(jfile)
    CourseInfo = None

    try:
        course = course.replace('-', ' ')
    except AttributeError:
        course = None

    for courseSection in courseDataList:
        if courseSection[0] == course:
            CourseInfo = courseSection

    return render_template("eng.html", cList=courseCheckList, CourseData=CourseInfo, major="software")

# Aerospace


@app.route('/aerospace')
def aerospace_page():
    return aerospace_page_link(None)


@app.route('/aerospace/<course>')
def aerospace_page_link(course):

    jfile = open("app/CourseDataOptimized/EECSOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("app/EngCrs/spaceCheck.json")
    courseCheckList = json.load(jfile)
    CourseInfo = None

    try:
        course = course.replace('-', ' ')
    except AttributeError:
        course = None

    for courseSection in courseDataList:
        if courseSection[0] == course:
            CourseInfo = courseSection

    return render_template("eng.html", cList=courseCheckList, CourseData=CourseInfo, major="aerospace")

# Electrical


@app.route('/electrical')
def electrical_page():
    return electrical_page_link(None)


@app.route('/electrical/<course>')
def electrical_page_link(course):

    jfile = open("app/CourseDataOptimized/EECSOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("app/EngCrs/electricalCheck.json")
    courseCheckList = json.load(jfile)
    CourseInfo = None

    try:
        course = course.replace('-', ' ')
    except AttributeError:
        course = None

    for courseSection in courseDataList:
        if courseSection[0] == course:
            CourseInfo = courseSection

    return render_template("eng.html", cList=courseCheckList, CourseData=CourseInfo, major="electrical")

# Mechanical


@app.route('/mechanical')
def mechanical_page():
    return mechanical_page_link(None)


@app.route('/mechanical/<course>')
def mechanical_page_link(course):

    jfile = open("app/CourseDataOptimized/MECHOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("app/EngCrs/mechanicalCheck.json")
    courseCheckList = json.load(jfile)
    CourseInfo = None

    try:
        course = course.replace('-', ' ')
    except AttributeError:
        course = None

    for courseSection in courseDataList:
        if courseSection[0] == course:
            CourseInfo = courseSection

    return render_template("eng.html", cList=courseCheckList, CourseData=CourseInfo, major="mechanical")

@app.route('/report', methods=["POST", "GET"])
def report_page():
    if request.method == "POST":
        name = request.form["inputName"]
        email = request.form["inputEmail"]
        course = request.form["inputCourse"]
        eng = request.form["inputType"]
        description = request.form["inputAddition"]
        
        current_time = datetime.datetime.now()
        date = [str(current_time.year), str(current_time.month), str(current_time.day)]
        
        if "" in {name, email, course, eng}:
            return render_template("report.html", errorStatus = True, successStatus = False) #add error
        else: 
            with open('bugsList.json') as json_file:
                bugs = json.load(json_file)

            bugs.append([name, email, course, eng, date, description])

            with open("bugsList.json", "w") as json_file:
                json.dump(bugs, json_file)

            return render_template("report.html", errorStatus = False, successStatus = True) #add a thank you for the report
    return render_template("report.html", errorStatus = False, successStatus = False)

@app.route('/bugs')
def bug_page():
    with open('bugsList.json') as json_file:
        bugs = json.load(json_file)
    
    return render_template("bugs.html", bugsList = bugs)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

# [END gae_flex_quickstart]
