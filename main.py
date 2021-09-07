from types import prepare_class
from flask import Flask, redirect, url_for, render_template
import json
import logging

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

    jfile = open("CourseDataOptimized/CIVILOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("EngCrs/civilCheck.json")
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

    jfile = open("CourseDataOptimized/EECSOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("EngCrs/computerCheck.json")
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

    jfile = open("CourseDataOptimized/EECSOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("EngCrs/softwareCheck.json")
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

    jfile = open("CourseDataOptimized/EECSOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("EngCrs/spaceCheck.json")
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

    jfile = open("CourseDataOptimized/EECSOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("EngCrs/electricalCheck.json")
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

    jfile = open("CourseDataOptimized/MECHOpCourseData.json")
    courseDataList = json.load(jfile)
    jfile = open("EngCrs/mechanicalCheck.json")
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

@app.route('/report')
def report_page():
    return render_template("report.html")

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
