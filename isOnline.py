import requests
import sys
import re
import BeautifulSoup
handle = raw_input("Enter the handle ")
url = "http://codeforces.com/profile/" + handle
res = requests.get(url)
Bobject = BeautifulSoup.BeautifulSoup(res.text)
k = 1
IsOnline = False
for grab in Bobject.findAll('span' , style = re.compile('^color:')):
	k +=1
	if(k == 3):

		if(grab.get('style')[6:11] == 'green'):
			IsOnline = True
			print handle , " is online on codeforces"
Bobject = BeautifulSoup.BeautifulSoup(res.text)
if(IsOnline == False):
	for grab in Bobject.findAll('span'):
		if grab.get('class') == 'format-humantime':
			print handle , 'was online ' , grab.text
			break
