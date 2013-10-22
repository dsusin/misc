from BeautifulSoup import BeautifulSoup
import urllib2

for i in range(20):
	url='http://www.alexa.com/topsites/countries;'+str(i)+'/ES'
	page=urllib2.urlopen(url)
	soup=BeautifulSoup(page.read())
	sites=soup.findAll('span', {'class':'small topsites-label'})
	for site in sites:
		print(site.string)
