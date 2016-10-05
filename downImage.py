import BeautifulSoup
import re
import requests
doOnit = ''
handle = raw_input("Enter The Handle")

fp = open("Photo.jpg" ,"wb")
res = requests.get("http://codeforces.com/profile/" + handle);
Bobject = BeautifulSoup.BeautifulSoup(res.text)
for grab in Bobject.findAll('img'):
	link = grab.get('src')
	if(link == 'http://codeforces.com/userphoto/title/'+handle+'/photo.jpg'):
		doOnit = link
		break
res2 = requests.get(doOnit)
for chunk in res2.iter_content(10000):
	fp.write(chunk)
fp.close()