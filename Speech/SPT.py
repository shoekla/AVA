import speech_recognition as sr
import os
import time
import Config
import sys
import Web
import CAL
import urllib2
import re
import nltk
import csv
import time
import requests
import string
from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
import fire
import webbrowser
import ApiAiAva
voice = Config.voice
name = Config.name
def say(s):
    os.system("print -v "+voice+" "+str(s))
def convo():
    counter = 0
    r = sr.Recognizer()
    userIn = ""
    with sr.Microphone() as source:
        print("print Ava:")
        audio = r.listen(source)
    try:
        userIn = str(r.recognize_google(audio))
    except sr.UnknownValueError:
        counter = counter+1;
        userIn = "noR"
        if (counter == 2):
            counter = 0
            #print("Good Bye")
            userIn = "shutdown"
    except sr.RequestError as e:
        counter = counter+1;
        userIn = "noR"
        if (counter == 2):
            counter = 0
            #print("Good Bye")
            userIn = "shutdown"
    print userIn
    return userIn

def getAndExecCommand():
    # obtain audio from the microphone
    counter = 0
    r = sr.Recognizer()
    userIn = ""
    with sr.Microphone() as source:
        print("print Command!")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        userIn = str(r.recognize_google(audio))
    except sr.UnknownValueError:
        counter = counter+1;
        userIn = "noR"
        if (counter == 2):
            counter = 0
            print("Good Bye")
            userIn = "shutdown"
    except sr.RequestError as e:
        counter = counter+1;
        userIn = "noR"
        if (counter == 2):
            counter = 0
            print("Good Bye")
            userIn = "shutdown"
    print "You Said: "+userIn

    userIn = userIn.lower()
    if ("hello" == userIn or "hey" == userIn or "hi" == userIn):
        print("Hi "+name+", I am Ava, a beers personal assistant")
    elif (userIn == "shutdown"):
        print("Good Bye")
    elif ("info on" in userIn or "information on" in userIn or "information about" in userIn or "look up" in userIn):
        begin = userIn.find("info")
        index = userIn.find(" ",userIn.find(" ",begin+1)+1)
        print("Pulling up information on "+userIn[index:])
        Web.infoOn(userIn[index:])
    elif ("video" in userIn):
        begin = userIn.find("video")
        index = userIn.find(" ",userIn.find(" ",begin+1)+1)
        print("Pulling up videos on "+userIn[index:])
        Web.openInWeb(Web.getYoutubeLink(userIn[index:]))
    elif ("play" in userIn):
        if "on youtube" in userIn:
            s = userIn[userIn.find(" ",userIn.find("play")):]
            s = s.replace("on youtube","")
            print ("Playing "+s)
            Web.music(s)
            return
        s = Web.getSubject(userIn)
        print s
        print ("Playing "+s)
        Web.music(s)
    elif (len(userIn) == 0):
        counter = counter+1;
        if (counter == 2):
            counter = 0
            print("Good Bye")
            userIn = "shutdown"
    elif ("definition" in userIn or "mean" in userIn):
        s = Web.definition(userIn)
        print(s)
    elif ("nor" == userIn):
        pass
    elif ("remind me to" in userIn):
        index = userIn.find("remind me to")
        begin = userIn.find(" ",index+len("remind me to"))
        re = userIn[begin:]
        if "comes out" in userIn:
            re = re.replace("watch","")
            re = re.replace("go to","")
            re = re.replace("when it comes out","") + "film "
            re = "Watch " +re + Web.getMovieDate(re)
            
            re = re.replace("film","")

        CAL.createEvent(re)
        print re
        print("ok i will remind you to "+re)
    elif ("give me searches" in userIn):
        userIn.strip()
        userIn = userIn[len("give me searches for"):]
        if ("youtube" in userIn):
            userIn = userIn.replace("on youtube","")
            userIn = userIn.replace("youtube","")
            print("Getting searches for "+userIn+"on youtube")
            Web.youtubeSearchs(userIn)
            return
        print("Getting searches for "+userIn+"on google")
        Web.openInWeb(Web.googLink(userIn))
    elif ("open" in userIn and "chrome" in userIn):
        print("Opening new Window in chrome")
        Web.openWindow()

    else:
        print("I did not understand that.")


"""
while True:
    if convo() == "Ava" or convo == "Eva":
        getAndExecCommand()
    else:
        print "No Ava"
print "Reached"
sys.exit(0)


"""
userIn ="begin"
subject = ""
while userIn != "":
    userIn = raw_input("Speak to AVA: ")
    userIn = userIn.replace("he",subject).replace("she",subject).replace("him",subject).replace("her",subject).replace("his",subject)

    if ("info on" in userIn or "information on" in userIn or "information about" in userIn or "look up" in userIn):
        begin = userIn.find("info")
        index = userIn.find(" ",userIn.find(" ",begin+1)+1)
        print("Pulling up information on "+userIn[index:])
        Web.infoOn(userIn[index:])
    elif ("video" in userIn):
        begin = userIn.find("video")
        index = userIn.find(" ",userIn.find(" ",begin+1)+1)
        print("Pulling up videos on "+userIn[index:])
        Web.openInWeb(Web.getYoutubeLink(userIn[index:]))
    elif ("play" in userIn):
        if "on youtube" in userIn:
            s = userIn[userIn.find(" ",userIn.find("play")):]
            s = s.replace("on youtube","")
            print ("Playing "+s)
            Web.music(s)
        s = Web.getSubject(userIn)
        print s
        print ("Playing "+s)
        Web.music(s)
    elif (len(userIn) == 0):
        counter = counter+1;
        if (counter == 2):
            counter = 0
            print("Good Bye")
            userIn = "shutdown"
    elif ("definition" in userIn or "mean" in userIn):
        s = Web.definition(userIn)
        print(s)
    elif ("nor" == userIn):
        pass
    elif ("remind me to" in userIn):
        index = userIn.find("remind me to")
        begin = userIn.find(" ",index+len("remind me to"))
        re = userIn[begin:]
        if "comes out" in userIn:
            re = re.replace("watch","")
            re = re.replace("go to","")
            re = re.replace("when it comes out","") + "film "
            re = "Watch " +re + Web.getMovieDate(re)
            
            re = re.replace("film","")

        CAL.createEvent(re)
        print re
        print("ok i will remind you to "+re)
    elif ("give me searches" in userIn):
        userIn.strip()
        userIn = userIn[len("give me searches for"):]
        if ("youtube" in userIn):
            userIn = userIn.replace("on youtube","")
            userIn = userIn.replace("youtube","")
            print("Getting searches for "+userIn+"on youtube")
            Web.youtubeSearchs(userIn)
        print("Getting searches for "+userIn+"on google")
        Web.openInWeb(Web.googLink(userIn))
    elif ("open" in userIn and "chrome" in userIn):
        print("Opening new Window in chrome")
        Web.openWindow()

    else:
        answer = Web.getAnswer(userIn)
        if answer != None and len(answer) > 0:
            subject = Web.getSubjectOfLine(userIn)
            print answer
        else:
            print ApiAiAva.apiAiResponse(userIn)




















