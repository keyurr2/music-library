# music-library

Online Music library to listen songs in your local environment and your friends can also listen if connected locally

## Getting Started

I have used two framework for this application 
1) Django - for serving web UI
2) Node js - for serving buffer audio file

### Prerequisites

To listen your favourite music individual or with you friends you need to install
1) Python (2.7.*)
2) Node js - stable version


### Installing

``` 
* [To install node js](https://nodejs.org/en/download/) - The javascript server framework
* [To install python](https://www.python.org/download/releases/2.7.2/) 
* After installing we need to install Django python package by 
* pip install django
```

## Running the project

In project directory you need to first start django server by 

```
python manage.py runserver
```

After starting django server we need to start app.js node script ... which you can find in folder
"rkmusic/static/library/music"

```
node app.js
```
You can run using nodemon module also.

