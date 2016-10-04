import requests 
import BeautifulSoup
import re
handle = raw_input("enter the handle")
url = "http://codeforces.com/profile/" + handle
res = requests.get(url)
Bobject = BeautifulSoup.BeautifulSoup(res.text)
for grab in Bobject.findAll('a' , href = re.compile('^/profile/' + handle)):
	if(grab.get('title') != 'None'):

		print "He is currently " ,grab.get('title')
