# Overview

The Trello board for this app can be found here: https://trello.com/b/88ms5t39/my-mood-diary

This app has been developed in consultation with clinical psychologists to track behaviours such as mood, diet, sleep, drug use, exercise as well as problem areas and skills.

Upon logging in, the user will be prompted to record their mood and emotions at that time which will be monitored and stored in a calendar.

It also allows users to add a daily journal entry and send a report to their therapist.

REST API end points can be found here: https://app.swaggerhub.com/apis/nerdypan/my-mood-diary/1.0.0 

The MVP (minimum viable product) for this application is the user authentication end points, client profile details including profile picture and add, updating, deleting and retrieving journal entries for the logged in user.

## Wireframes

The MVP includes the Login page, sign up page, profile page and the My Journal page below:
### Login page

![login page](docs/Login_page_wireframe.png)

### Sign up page

![Sign up page](docs/Sign_up_page_wireframe.png)

### Profile page

![Profile page](docs/Profile_wireframe.png)

### My Journal

https://material-ui.com/components/pickers/#datepickers

![My Journal](docs/Journal_wireframe.png)

Version 2 of this application will include:
### How are you feeling? and Emotions

![How are you feeling?](docs/How_are_you_feeling_Emotions_wireframe.png)
https://material-ui.com/components/slider/#discrete-sliders


### Actions

![Actions](docs/Actions_wireframe.png)

### Problem Areas

![Problem Areas](docs/Problem_areas_wireframe.png)

### Tracker Log

![Tracker Log](docs/tracker_log_wireframe.png)

### Skills

![Skills](docs/Skills_wireframe.png)

### Calendar

![Calendar](docs/Calendar_wireframe.png).

## Entity relationships

![Database Entity Relationships](docs/erd_v2.png).

## Instructions

The instructions for Ubuntu 20:

Update repositories on Ubuntu: `sudo apt-get update`

Clone GitHub repository: `git clone https://github.com/PandelisT/my-mood-diary.git`

Install python virtual environment: `sudo apt-get install python3.8-venv`

Create virtual environment: `python3.8 -m venv venv`

Activate the virtual environment `source venv/bin/activate`

Install pip: `python -m pip install --upgrade pip`

Install modules from requirements.txt: `pip install -r requirements.txt`