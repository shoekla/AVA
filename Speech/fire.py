
from firebase import firebase
import random
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
import webbrowser
firebase = firebase.FirebaseApplication('https://jacbis.firebaseio.com/', None)
"""result = firebase.get('s', None)
if result == None:
	print "Nothing Found :("
else:
	print result
"""
global randomR
global conv
conv = []
conv.append("(ME)Hey what's up?")
def getMe():
	return conv
def putInFirebase(phrase,response):
	phrase = phrase.lower()
	phrase = phrase.strip()
	if getResp(phrase) == None:
		response = "['"+response+"']"
		firebase.post(phrase,response)
		keys = eval(getResp("Keys"))
		keys.append(phrase)
		firebase.delete("Keys",None)
		firebase.post("Keys",str(keys))
		incrementN()
		return 1
	else:
		print "1"
		a = eval(getResp(phrase))
		r = eval(getResp(phrase))
		for item in r:
			print "Item: "+item + "Res: "+response
			if item == response:
				return len(a)
		print "2"
		a.append(response)
		print "3"
		firebase.delete(phrase,None)
		print "4"
		firebase.post(phrase,str(a))
		print "5"	
		incrementN()
		return len(a)
def putInFirebasePython(phrase,response):
	phrase = phrase.lower()
	phrase = phrase.strip()
	if getResp(phrase) == None:
		response = "['"+response+"']"
		firebase.post(phrase,response)
		keys = eval(getResp("PythonKeys"))
		keys.append(phrase)
		firebase.delete("PythonKeys",None)
		firebase.post("PythonKeys",str(keys))
		incrementN()
		return 1
	else:
		print "1"
		a = eval(getResp(phrase))
		r = eval(getResp(phrase))
		for item in r:
			print "Item: "+item + "Res: "+response
			if item == response:
				return len(a)
		print "2"
		a.append(response)
		print "3"
		firebase.delete(phrase,None)
		print "4"
		firebase.post(phrase,str(a))
		print "5"	
		incrementN()
		return len(a)

def addToConvYou(phrase):
	w = phrase.lower()
	phrase = "(YOU)"+phrase
	conv.append(phrase)
	print "YYYYYys"
	getMyResp(w)
def getRandR():
	arr = eval(getResp('randomR'))
	return arr
def getRandomResponse():
	arr = getRandR()
	res = arr[random.randint(0, len(arr)-1)]
	return res

def addToRand(phrase):
	arr = eval(getResp('randomR'))
	if phrase not in arr:
		arr.append(phrase)
		firebase.delete('randomR',None)
		firebase.post('randomR',str(arr))
		return 'green'
	return 'red'
def getMyResp(p):
	keys  = eval(getResp("Keys"))
	for item in keys:
		if item in p:
			arrR = eval(getResp(item))
			resP = arrR[random.randint(0, len(arrR)-1)]
			b = resP[1:]
			return b
	return ""
def getMyResp(p):
	keys  = eval(getResp("Keys"))
	for item in keys:
		if item in p:
			arrR = eval(getResp(item))
			resP = arrR[random.randint(0, len(arrR)-1)]
			b = resP[1:]
			return b
	return ""

def getResp(phrase):
	a = firebase.get(phrase,None)
	if a == None:
		return None
	keys = []
	for key in a:
		"""
		print "key: %s , value: %s" % (key, a[key])
		"""
		keys.append(key)
	return a[keys[0]]
def getKey(phrase):
	a = firebase.get(phrase,None)
	if a == None:
		return None
	keys = []
	for key in a:
		"""
		print "key: %s , value: %s" % (key, a[key])
		"""
		keys.append(key)
	return keys[0]
def incrementN():
	a = firebase.get("NumOfPhrases",None)
	print a
	keys = []
	count = 0
	for key in a:
		"""
		print "key: %s , value: %s" % (key, a[key])
		"""
		keys.append(key)
		count = count +1
	i = int(a[keys[count-1]])
	i = i+1
	firebase.delete('NumOfPhrases',None)
	firebase.post("NumOfPhrases",str(i))
def getRandLen():
	arr = eval(getResp('randomR'))
	return len(arr)
def getMyRespPyth(p):
	keys  = eval(getResp("PythonKeys"))
	for item in keys:
		if item in p:
			arrR = eval(getResp(item))
			resP = arrR[random.randint(0, len(arrR)-1)]
			b = resP[1:]
			res = ""
			exec(b)
			print "Res: "+res
			return res
	return ""
"""
a = ["Hey"]
b = a[random.randint(0, len(a)-1)]
print b

arr = eval(getResp('randomR'))
print arr[0]
"""
