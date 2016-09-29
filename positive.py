import urllib
import urllib2
import BeautifulSoup
import re


name=str(raw_input('enter your codeforces Id !!'))
mainURL="http://www.codeforces.com/contests/with/" + name 
 
print mainURL

response = urllib2.urlopen(mainURL)
soup = BeautifulSoup.BeautifulSoup(str(response.read()))
tab = 1
for grab in soup.findAll('a', href=re.compile('^/contest/')):
    tab=tab+1
    if tab%2==0:
    	print ("contest name : " + grab.text),
    else:
    	print ("contest rank  was -> ! " +  grab.text)
