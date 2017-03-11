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

def openInWeb(url):
	print "In ethod"
	# Open URL in new window, raising the window if possible.
	webbrowser.open_new(url)
def openWindow():
	webbrowser.open("https://www.google.com/", new=2, autoraise=True)
def is_in_arr(lis,s):
	result=False
	for item in lis:
		if item==s:
			result=True
	return result
def deleteDuplicates(lis):
	newLis=[]
	for item in lis:
		if item not in newLis:
			newLis.append(item)
	return newLis

def getData(url):
	try:

		regex='<p>(.+?)</p>'
		headers='Info In Paragrapgh'

		pattern = re.compile(regex);
		htmlfile=urllib2.urlopen(str(url))
		htmltext=htmlfile.read()
		title=re.findall(pattern,htmltext)
		if len(str(title))>=1:
			return title
		else:
			return "nothing"
	except:
		print "Data Error At "+str(url)

def getName(url):

	regex='<title>(.+?)</title>'
	headers='Title:'
	pattern = re.compile(regex);
	htmlfile=urllib2.urlopen(url)
	htmltext=htmlfile.read()
	title=re.findall(pattern,htmltext)
	for college in colleges:
		if college in str(title):
			str(title).replace(college,"")
	return title
def getGoodLink(url):
	k = url.rfind("/")
	return url[:k+1]
def getHTML(url):
	try:
		htmlfile=urllib2.urlopen(str(url))
		htmltext=htmlfile.read()
		htmltext.replace("<!Doctype html>","")
		htmltext.replace("<html","")
		htmltext.replace("</html>","")
		tokens = nltk.word_tokenize(htmltext)
		return tokens
	except:
		return "Error Occured"
#nltk.download()
def checkNum(num):
	num=num[7:]
	if len(num)==10:
		for item in num:
			if str(item).isalpha():
				return False
			elif "1" not in item and "2" not in item and "3" not in item and "4" not in item and "5" not in item and "6" not in item and "7" not in item and "8" not in item and "9" not in item and "0" not in item: 
				return False
			else:
				return True
	elif len(num)==12:
		d=0
		first=num[:3]
		second=num[4:7]
		third=num[8:13]
		for item in first:
			if str(item).isalpha():
				d=1
			elif "1" not in item and "2" not in item and "3" not in item and "4" not in item and "5" not in item and "6" not in item and "7" not in item and "8" not in item and "9" not in item and "0" not in item: 
				d=1
			else:
				pass
		for item in second:
			if str(item).isalpha():
				d=1
			elif "1" not in item and "2" not in item and "3" not in item and "4" not in item and "5" not in item and "6" not in item and "7" not in item and "8" not in item and "9" not in item and "0" not in item: 
				d=1
			else:
				pass
		for item in third:
			if str(item).isalpha():
				d=1
			elif "1" not in item and "2" not in item and "3" not in item and "4" not in item and "5" not in item and "6" not in item and "7" not in item and "8" not in item and "9" not in item and "0" not in item: 
				d=1
			else:
				pass
		if d==0:
			return True
		else:
			return False
	else:
		return False

def getPhone(url):
	try:
		tokens=getHTML(url)
		nums=[1,2,3,4,5,6,7,8,9,0]
		contacts=[]
		string=""

		for i in range(0,len(tokens)):
			item=tokens[i]
			if len(item)==10:
				number=True

				if item.isalpha():
					number=False

				if item[3:6]=="555":
					number=False

				if str(item[0])!="1" or str(item[0])!="2" or str(item[0])!="3" or str(item[0])!="4" or str(item[0])!="5" or str(item[0])!="6" or str(item[0])!="7" or str(item[0])!="8" or str(item[0])!="9" or str(item[0])!="0":
					number=False
				if number==True and item not in contacts:
					contacts.append(item)
			if len(item)==12:
				number=True
				"""
				if item[3]!= "-" or item[7]!="-":
					if item[3]!="." or item[7]!=".":
						number=False
				"""
				if str(item[0]).isalpha() or str(item[1]).isalpha() or str(item[2]).isalpha() or str(item[3]).isalpha() or str(item[4]).isalpha() or str(item[5]).isalpha() or str(item[6]).isalpha() or str(item[7]).isalpha() or str(item[8]).isalpha() or str(item[9]).isalpha() or str(item[10]).isalpha() or str(item[11]).isalpha():
					number=False
				if item[4:7]=="555":
					number=False

				if number==True and item not in contacts:
					if "Fax" in tokens[i-2]:
						contacts.append("Fax: "+item)
					else:
						contacts.append("Phone: "+item)
			resCon=[]
			for item in contacts:
				if checkNum(str(item)):
					resCon.append(item)
		return resCon
	except:
		return "Error Occured"

def getEmail(url):
	try:
		tokens=getHTML(url)
		contacts=[]
		for i in range(0,len(tokens)):
			if "@" in tokens[i]:
				string= str(tokens[i-1])
				if string[0].isalpha():
					string = string +str(tokens[i])
					string = string +str(tokens[i+1])
					endA=str(tokens[i+1])
					if endA.find(".")>=0:
						if is_in_arr(contacts,tokens[i])==False:
							if string.endswith(".")==False:
								contacts.append(string)
			if "at"==tokens[i]:
				if tokens[i-1]=="[" and tokens[i+1]=="]":
					string=str(tokens[i-2])+"@"+str(tokens[i+2])
					contacts.append(string)
			if len(tokens[i])==3:
				if tokens[i].isalpha==False:
					if (tokens[i+1].isalpha==False and len(tokens[i+1])==3) and (tokens[i+2].isalpha()==False and len(tokens[i+2])==3) and item not in contacts:
						string = str(tokens[i]) +str(tokens[i+1])+str(tokens[i+2])
						contacts.append("Email: "+string)
		new = deleteDuplicates(contacts)
		return new
	except:
		return "Error Occured"

def crawl(url,pages):
	try:
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('a'):

			href=link.get('href')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if is_in_arr(pages,str(href))==False:
				if "microsoft" not in href_test and "facebook" not in href_test and "twitter" not in href_test:
					if href_test.startswith("http"):
						pages.append(str(href))
					else:
						lin=getGoodLink(url)
						pages.append(lin+str(href))

	except:
		print "Error at: "+str(url)


def contactLink(url):
	try:
		pages=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('a'):

			href=link.get('href')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if is_in_arr(pages,str(href))==False:
				if "microsoft" not in href_test and "facebook" not in href_test and "twitter" not in href_test:
					if href_test.startswith("http"):
						pages.append(str(href))
					else:
						lin=getGoodLink(url)
						pages.append(lin+str(href))

	except:
		print "Error at: "+str(url)






def crawlLink(ina):
	links=[]
	item=ina
	crawl(item,links)
	new=deleteDuplicates(links)
	return new

def crawlLinkScoial(url):
	try:
		pages=[]
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('a'):

			href=link.get('href')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if is_in_arr(pages,str(href))==False:
				if "facebook" in href_test or "twitter" in href_test or "google" in href_test:
					pages.append(str(href))
		newArr=deleteDuplicates(pages)
		return newArr



	except:
		print "Error at: "+str(url)
def getGoogLink(url):
	arr=crawlLinkScoial(url)
	a=[]
	for item in arr:
		if "google" in item:
			a.append(item)
	try:
		return a[0]
	except:
		link = url.replace(":","%3A")
		link = link.replace("/","%2F")
		return getGooglePlus(link)
def getTwitLink(url):
	arr=crawlLinkScoial(url)
	a=[]
	for item in arr:
		if "twitter" in item:
			a.append(item)
	try:
		return a[0]
	except:
		link = url.replace(":","%3A")
		link = link.replace("/","%2F")
		return getTwitter(link)
def getFaceLink(url):
	arr=crawlLinkScoial(url)
	a=[]
	for item in arr:
		if "facebook" in item:
			if item!="http://facebook.com":
				a.append(item)

	try:
		return a[0]
	except:
		link = url.replace(":","%3A")
		link = link.replace("/","%2F")
		return getFacebook(link)


def contact(url):
	phone=getPhone(url)
	email=getEmail(url)
	second=[]
	for item in phone:
		second.append(str(item))
	for item in email:
		second.append(str(item))
	new=deleteDuplicates(second)
	resFile.write(url+"\n \n")
	for item in new:
		if len(item)>=1:
			resFile.write(item)
			resFile.write("\n")	
		else:
			resFile.write("No Contacts on this Link")
			resFile.write("\n")
	if len(new)>=1:
		contactFile.write("No contacts on "+str(url))
		allFile.write("No contacts on "+str(url))
		allSocial.write("No contacts on "+str(url))

def contactSearch(urls):
	second=[]
	for url in urls:
		print str(url)
		phone=getPhone(url)
		email=getEmail(url)
		third=[]
		third.append(url)
		third.append(phone+email)
		second.append(third)
	new=deleteDuplicates(second)
	return new


def link(url):
	crawlLink(url)
	crawlLinkScoial(url)
	contact(url)
	data=getData(url)
	dataFile.write(str(data))
	allFile.write("Data Aggregated: \n")
	allFile.write(str(data))
	allSocial.write("Data Aggregated: \n")
	allSocial.write(str(data))

def getDataLink(url):
	c=[]
	res=[]
	data=getData(url)
	if data!="nothing":
		c.append(str(url))
		c.append(str(data))
		res.append(c)
		return res
	return "No Results for "+str(url)
def isLink(url):
	if str(url).startswith("http"):
		return True
	return False
def turnToSearch(text):
	search=text.replace(" ","%20")
	link="http://www.bing.com/search?q="+str(search)+"&qs=n&form=QBRE&pq="+str(search)+"&sc=9-6&sp=-1&sk=&cvid=6585c559beef41f3b942271b982e674a"
	return link
def crawlSearch(url,pages):
	try:
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('a'):

			href=link.get('href')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if is_in_arr(pages,str(href))==False:
				if "microsoft" not in href_test and "facebook" not in href_test and "twitter" not in href_test and "google" not in href_test:
					if href_test.startswith("http"):
						if "bing" not in href_test:
							pages.append(href)
					else:
						pass


	except:
		print "Error at: "+str(url)
def getMoreSearch(url):
	try:
		pages=[]
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		pages.append(str(url))
		for link in soup.findAll('a'):

			href=link.get('href')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if href_test.startswith("/search"):
				if "microsoft" not in str(url) and "microsoft" not in href_test:
					pages.append(str(url+href))

		return pages
	except:
		return []

def takeOutBing(arr):
	new=[]
	for ite in arr:
		item=str(ite)
		if "bing" not in item:
			new.append(ite)
	return new



def getLinksFromS(url):
	link=turnToSearch(str(url))
	a=getMoreSearch(link)
	b=[]
	for item in a:
		crawlSearch(item,b)
		print item
	for item in b:
		linkText.write(item)
		linkText.write("\n")

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)
def findWhatToScrape(arr):
	new=[]
	testArr=[]
	for s in arr:
		begin=findnth(s,"/",1)
		end=findnth(s,"/",2)
		item=s[begin+1:end]
		if item not in testArr:
			testArr.append(item)
			new.append(s)
	return new

def searchQ(link):
	url=turnToSearch(str(link))
	b=getMoreSearch(url)
	a=[]
	for item in b:
		crawlSearch(item,a)
	for item in a:
		print item
		linkText.write(str(item))
		linkText.write("\n")	
	scrapes=findWhatToScrape(a)
	for item in scrapes:
		print item
		contactFile.write(str(item)+"\n")
		contact(item)
	allSocial.write("Data Aggregated: \n")
	allFile.write("Data Aggregated: \n")
	for item in scrapes:
		print item
		data=getData(item)
		dataFile.write(str(item))
		allFile.write("\n \n")
		dataFile.write(str(data))
		allFile.write("\n \n")
		allFile.write(item+"\n")
		allFile.write(str(data))
		allFile.write("\n \n")
		allSocial.write(item+"\n")
		allSocial.write(str(data))
		allSocial.write("\n \n")
def getDataTwo(url):
	htmlfile=urllib2.urlopen(url)
	htmltext=htmlfile.read()
	soup = BeautifulSoup(htmltext)
	please=soup.get_text().strip()
	res=please.split('\n')
	resA=[]
	for item in res:
		r=item.strip(" ")
		if len(r)>=1:
			if "wiki" in url:
				if r.endswith("]") and " " in r:
					resA.append(removeBrac(str(r)))
			else:
				resA.append(r)
	finaR=[[[url],['\n'.join(resA)]]]
	return finaR
def removeBrac(para):
	while True:
		if para.find("[")>=0:
			begin=para.find("[")
			end=para.find("]",begin)
			para=para.replace(para[begin:end+1],'')
			#print "Deleteing"
		else:
			break
	return para
def removePra(para):
	while True:
		if para.find("(")>=0:
			begin=para.find("(")
			end=para.find(")",begin)
			para=para.replace(para[begin:end+1],'')
			#print "Deleteing"
		else:
			break
	return para

def getDataThree(url):
	htmlfile=urllib2.urlopen(url)
	htmltext=htmlfile.read()
	soup = BeautifulSoup(htmltext)
	please=soup.get_text().strip()
	res=please.split('\n')
	resA=[]
	for item in res:
		r=item.strip(" ")
		if len(r)>=1:
			if "wiki" in url:
				if r.endswith("]") and " " in r:
					resA.append(removeBrac(str(r)))
			else:
				resA.append(r)

	finaR=[[url],['\n'.join(resA)]]
	return finaR
def SearchCrawl(link):
	url=turnToSearch(str(link))
	b=getMoreSearch(url)
	a=[]
	for item in b:
		crawlSearch(item,a)
	return a
def SearchCrawlPDF(link):
	link=str(str(link)+" PDF")
	url=turnToSearch(str(link))
	b=getMoreSearch(url)
	a=[]
	for item in b:
		crawlSearch(item,a)
	c=[]
	for item in a:
		if str(item).endswith("pdf"):
			c.append(item)
	d=deleteDuplicates(c)
	return d
def crawlPDF(link):
	a=[]
	crawl(link,a)
	b=[]
	for item in a:
		if str(item).endswith("pdf"):
			print item
			b.append(item)
	c=deleteDuplicates(b)
	return c

def turnToWiki(link):
	search=link.replace(" ","+")
	link="https://en.wikipedia.org/w/index.php?search="+str(search)+"&title=Special%3ASearch&go=Go"
	return link

def SearchInfo(link):
	url=turnToSearch(str(link))
	a=[]
	res=[]
	c=[]
	crawlSearch(url,a)
	for item in a:
		c=[]
		try:
			c=getDataThree(str(item))
			res.append(c)
			print "Good at: "+str(item)
		except:
			print "Error at: "+str(item)
	return res
def SearchContact(link):
	url=turnToSearch(str(link))
	b=getMoreSearch(url)
	a=[]
	for item in b:
		print "crawling"
		crawlSearch(item,a)
	resA=contactSearch(a)
	return resA
def SearchSocial(link):
	search=link.replace(" ","%20")
	twit="https://twitter.com/search?f=users&vertical=default&q="+str(search)+"&src=typd"
	aa=[]
	a=[]
	crawl(twit,aa)
	for link in aa:
		if "?lang=" not in str(link):
			a.append(link)
	goog="https://plus.google.com/s/"+str(search)
	search=link.replace(" ","%2B")
	face="https://www.facebook.com/search/str/"+str(search)+"/keywords_top"
	b=[]
	crawl(face,b)
	for item in b:
		a.append(item)
	c=[]
	crawl(goog,c)
	for item in c:
		a.append(item)
	new=deleteDuplicates(a)
	return new
def getTwitter(link):
	search=link.replace(" ","%20")
	twit="https://twitter.com/search?f=users&vertical=default&q="+str(search)+"&src=typd"
	return twit


def getFacebook(link):
	search=link.replace(" ","%2B")
	face="https://www.facebook.com/search/str/"+str(search)+"/keywords_top"
	return face
def getGooglePlus(link):
	search=link.replace(" ","%20")
	goog="https://plus.google.com/s/"+str(search)
	return goog

def contactLink(url):
	email=getEmail(url)
	phone=getPhone(url)
	resA=email+phone
	res=deleteDuplicates(resA)
	fin=[[[url],res]]
	return fin
def contactLinkTwo(url):
	email=getEmail(url)
	phone=getPhone(url)
	resA=email+phone
	res=deleteDuplicates(resA)
	if len(res)>=1:
		fin=[[url],[res]]
		return fin
	else:
		return "noth"
def contactsA(link):
	url=turnToSearch(str(link))
	a=[]
	res=[]
	c=[]
	crawlSearch(url,a)
	for item in a:
		fin=[]
		try:
			fin=contactLinkTwo(item)
			if fin!="noth":
				res.append(fin)
			print "Good Contact at: "+str(item)
		except:
			print "Error Contact: "+str(item)
	return res



def removeHtml(para):
	while True:
		if para.find("<")>=0:
			begin=para.find("<")
			end=para.find(">",begin)
			para=para.replace(para[begin:end+1],'')
		else:
			break
	return para
#print removeHtml('<a h="ID=SERP,5305.1" href="/search?q=george+w.+bush&amp;filters=ufn%3a%22george+w.+bush%22+sid%3a%22b8205878-34f8-6339-c1ab-1f26c061dfe7%22&amp;FORM=SNAPST">George W. Bush</a>')
#print removeHtml("Hello World")
def crawlImg(url,pages):
	try:
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('img'):

			href=link.get('src')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if is_in_arr(pages,str(href))==False:
				if "1.1" in href:
					pages.append(href)


	except:
		print "Error at: "+str(url)
def linkImg(url):
	try:
		pages=[]
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('img'):

			href=link.get('src')
			href_test=str(href)
			#if href_test[0]!='/' and href_test[0]!='j' and href_test!='none' and href_test[0]!='#':
			if is_in_arr(pages,str(href))==False:
				if href.startswith("http"):
					pages.append(href)
				else:
					pages.append(str(url+href))
		return pages

	except:
		return []
		print "Error at: "+str(url)
def searchImg(link):
	search=link.replace(" ","+")
	link="http://www.bing.com/images/search?q="+str(search)+"&FORM=HDRSC2"
	a=[]
	crawlImg(link,a)
	new=deleteDuplicates(a)
	return new
def searchImgGoogle(name):
	search=name.replace(" ","+")
	link="https://www.google.com/search?q="+search+"&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi67cG4rcTPAhUJ7oMKHV_ZCjcQ_AUICygE&biw=1920&bih=983"
	return link
def getYoutubeLink(name):
	search = name.replace(" ","+")
	url="https://www.youtube.com/results?search_query="+str(search)
	return url
def getVideoSearch(link):
	search=link.replace(" ","+")
	a=[]
	url="https://www.youtube.com/results?search_query="+str(search)
	crawl(url,a)
	b=[]
	c=[]
	for item in a:
		if "/watch" in item:
			b.append(item)
	for item in b:
		c.append(str("https://www.youtube.com/embed/"+str(item[33:])))
	new=deleteDuplicates(c)
	return new
def getMusic(link):
	link=str(str(link)+" Lyrics")
	search=link.replace(" ","+")
	a=[]
	url="https://www.youtube.com/results?search_query="+str(search)
	crawl(url,a)
	b=[]
	c=[]
	for item in a:
		if "/watch" in item:
			b.append(item)
	for item in b:
		c.append(str("http://www.youtube-mp3.org//get?video_id="+str(item[33:])+"&ts_create=1438960796&r=MjA5LjExNi4yMjguODI%3D&h2=6d407dbe28487282810f9eb1ef8c841b&s=139712"))
		#/get?video_id=KMU0tzLwhbE&ts_create=1438960796&r=MjA5LjExNi4yMjguODI%3D&h2=6d407dbe28487282810f9eb1ef8c841b&s=139712
	new=deleteDuplicates(c)
	return new

def linkVid(url):
	try:
		pages=[]
		htmlfile=urllib2.urlopen(str(url))
		htmltext=htmlfile.read()
		"""while True:
			if htmltext.find("<iframe")>=0:
				print "Getting"
				begin=htmltext.find("<iframe")
				end=htmltext.fins(">",begin)
				srcBegin=htmltext.find("src",begin,end)
				srcEnd=htmltext.find('"',srcBegin,end)
				pages.append(htmltext[srcBegin:srcEnd+1])
				htmltext=htmltext.replace(htmltext[begin:end+1],"")
			else:
				break
		return pages
		"""
		while True:
			s=htmltext.find("embed")
			if s>=1:
				print"Getting Vids"
				fd=htmltext.find('"',s)
				if str(htmltext[s:fd]).startswith("http"):
					pages.append(str(htmltext[s:fd]))
				else:
					pages.append(str("https://www.youtube.com/"+htmltext[s:fd]))
				htmltext=htmltext.replace(htmltext[s:fd],"")
			else:
				break
			d=[]
			for page in pages:
				try:
					#d.append(page[:page.find("&amp")])
					pass
				except:
					pass
			new=deleteDuplicates(d)

		return d

	except:
		return []
		print "Error at: "+str(url)

def googLink(name):
	name = name.replace(" ","+")
	url = "https://www.google.com/search?q="+name+"&oq="+name+"&aqs=chrome..69i57.2831j0j7&sourceid=chrome&ie=UTF-8"
	return url
def infoOn(name):
	goog = googLink(name)
	facebook = getFacebook(name)
	twit = getTwitter(name)
	google =getGooglePlus(name)
	
	openInWeb(facebook)
	openInWeb(twit)
	openInWeb(google)
	openInWeb(turnToWiki(name))
	openInWeb(goog)

def getSubject(orName):
	try:
		name = orName.replace(" ","+")
		url = "http://www.bing.com/search?q="+name+"&qs=n&form=QBRE&pq="+name+"&sc=0-14&sp=-1&sk=&cvid=0BB6171F844942A19AF1C6F4837B3D26"
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		so = str(soup)
		index = so.find('<h2 class=" b_entityTitle">')
		if index == -1:
			name = name+"+ Band"
			url = "http://www.bing.com/search?q="+name+"&qs=n&form=QBRE&pq="+name+"&sc=0-14&sp=-1&sk=&cvid=0BB6171F844942A19AF1C6F4837B3D26"
			index = so.find('<h2 class=" b_entityTitle">')
		if index == -1:
			return orName
		end = so.find("</h2>",index)
		Song = so[index+27:end]
		if so.find('<span class="cbl b_lower">Artist') == -1:
			return "Songs by "+so[index+27:end]
		
		index = so.find("h=",so.find('<span class="cbl b_lower">Artist'))
		begin = so.find(">",index+1)
		end = so.find("</a>",index+1)
		Artist = so[begin+1:end]
		return Song+" by "+Artist
	except:
		pass

def music(name):
	if "Songs by" in name:
		name = name.replace(" ","+")
		link = "https://www.youtube.com/results?q="+name+"&sp=EgIQAw%253D%253D"
		a = []
		crawl(link,a)
		for i in a:
			if "&list" in i:
				openInWeb(i)
				return
		openInWeb(link)
		return
	name = name.replace(" ","+")
	link = "https://www.youtube.com/results?search_query="+str(name)
	a = []
	crawl(link,a)
	for i in a:
		if "/watch" in i:
			openInWeb(i)
			return
	openInWeb(link)
	return

def definition(word):
	url = turnToSearch(word)
	try:
		#print url
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		so = str(soup)
		#print so
		index = 0
		end = 0
		res = ""
		counter = 0
		while index > -1:
			index = so.find('<div class="dc_mn">',end)
			#print index
			begin = so.find('>',index+1)
			end = so.find('</div>',begin+1)
			counter = counter +1
			res = res+""+str(counter)+", "+so[begin+1:end]
			index = so.find('<div class="dc_mn">',end)
		res = res.replace(":","")
		res = res.replace("(","")
		res = res.replace(")","")
		if len(res) > 1:
			return res
		return "I could not understand that"

	except:
		pass

#print definition("What is the definition of music")


def getAnserInfo(name):
	try:
		name = name.replace(" ","+")
		url = "http://www.bing.com/search?q="+name+"&qs=AS&pq="+name+"&sc=8-19&sp=1&cvid=9464A3030C30444898E745A4763A0675&FORM=QBRE"
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('div'):
			if "rwrl rwrl_sec rwrl_padref" in str(link):
				s = removeHtml(str(link))
				s = s[s.find("?")+1:]
				arr = s.split(".")
				if len(arr) > 2:
					s = arr[0] + arr[1]
					if arr[1] == "Reference: en":
						return removeHtml(removeBrac(removePra(arr[0])))
					return removeHtml(removeBrac(removePra(s)))
				else:
					return removeHtml(removeBrac(removePra(arr[0])))
	except:
		"I can't answer that. Sorry"

#print getAnserInfo("sajdkfhasldjf")
def getSubjectOfLine(name):
	name = name.replace(" ","+")
	url = "http://www.bing.com/search?q="+name+"&qs=AS&pq="+name+"&sc=8-19&sp=1&cvid=9464A3030C30444898E745A4763A0675&FORM=QBRE"
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	for link in soup.findAll('h2'):
		if "b_entityTitle" in str(link) and "?" not in str(link):
			return removeHtml(str(link))
#print getSubject("who is bill gates")
#print getAnswer("When was albert eninsetiens birthday")
def getAnswer(name):
	name = name.replace(" ","+")
	url = "http://www.bing.com/search?q="+name+"&qs=AS&pq="+name+"&sc=8-19&sp=1&cvid=9464A3030C30444898E745A4763A0675&FORM=QBRE"
	try:
		#print url
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		so = str(soup)
		#print so
		index = 0
		end = 0
		res = ""
		index = so.find('class="b_focusText',end)
		#print index
		begin = so.find('>',index+1)
		end = so.find('</div>',begin+1)
		#print end
		res = so[begin+1:end]
		res = res.replace("(","")
		res = res.replace(")","")
		res= removeHtml(res)
		if len(res) > 1 and index != -1:
			return res
		return getAnserInfo(name)

	except:
		pass
	return getAnserInfo(name)
def getMovieDate(name):
	name = name +" release date"
	name=name.replace(" ","+")
	url = "http://www.bing.com/search?q="+str(name)+"&go=Submit&qs=n&form=QBLH&pq=the+avengers&sc=10-11&sp=-1&sk=&ghc=1&cvid=368740BF914F45C4A0459CD0D08B5CF6"
	try:
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		so = str(soup)
		index = so.find('<div class="b_focusText')
		begin = so.find(">",index)+1
		end = so.find("</div>",index+1)
		so = so[begin:end]
		#print "So: "+so
		if len(so) == 0:
			so = str(soup)
			index = so.find(">",so.find("Release date:</span>"))
			end = so.find("</li>")
			so = so[index:end]
		so = so.replace("(United States)","")
		return so

	except Exception,e: print str(e)

def youtubeSearchs(name):
	name = name.replace(" ","+")
	link = "https://www.youtube.com/results?search_query="+str(name)
	openInWeb(link)


