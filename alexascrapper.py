from BeautifulSoup import BeautifulSoup
import urllib2
import sys
import os

url = "http://www.alexa.com"
topsite = "/topsites/countries"
globalurl = "/topsites/global;"
path = "countryList/"

b = False
x = 500;

def usage():
    print "\nAlexasScrapper\n\nUsage:\n"
    print "python alexascrapper.py [-h] [-g [X]] [-c [X]]"
    print "\nWithout options: \t Prints top 500 sites on the web by Country."
    print "\n-h:\tHelp - prints this usage."
    print "-c:\tPrints top X sites on the web by Country."
    print "-g:\tPrints global top X sites on the web."
    print " \t\t1 <= X <= 500"

    sys.exit(0)


def init_args():
    global b
    global x
    if len(sys.argv) == 1:
        b = True
    elif len(sys.argv) >= 2:
        if sys.argv[1] == '-g':
            b = False
            if len(sys.argv) == 3:
                try:
                    x = int(sys.argv[2])
                    if x > 500 or x < 1:
                        usage()
                except:
                    usage()
        elif sys.argv[1] == '-c':
            b = True
            if len(sys.argv) == 3:
                try:
                    x = int(sys.argv[2])
                    if x > 500 or x < 1:
                        usage()
                except:
                    usage()
        else:
            usage()
    else:
        usage();

def global_search():

    count = 0

    for i in range(20):


        urlF=url + globalurl + str(i)

        page=urllib2.urlopen(urlF)
        soup=BeautifulSoup(page.read())

        sect = soup.findAll('section')
        fsec = None
        for s in sect:
            if s['class'] == "td col-r":
                fsec = s
        sites=fsec.findAll('li')
        for site in sites:
            if count == x:
                break

            count += 1;
            print str(count) + "- "+site.a.string

        if count == x:
            break


def get_sites_by_country(country,final_url):
    print country + ":"
    count = 0

    create_directory()

    f = open(path+country + ".txt", 'w')

    for i in range(20):
        urlF = url + topsite + ";" + str(i) + "/" + final_url

        page=urllib2.urlopen(urlF)
        soup=BeautifulSoup(page.read())

        sect = soup.findAll('section')
        fsec = None
        for s in sect:
            if s['class'] == "td col-r":
                fsec = s
        sites=fsec.findAll('li')
        for site in sites:
            if count == x:
                break

            count += 1;
            print str(count) + "- "+site.a.string
            f.write(site.a.string + "\n")

        if count == x:
            break


def by_countries():

    urlF= url + topsite

    page=urllib2.urlopen(urlF)
    soup=BeautifulSoup(page.read())

    sect = soup.findAll('section')
    fsec = None
    for s in sect:
        if s['class'] == "td col-r":
            fsec = s
    sites=fsec.findAll('li')
    for site in sites:
        final_url =  site.a.get('href').split('/')[3]
        country = site.a.string
        get_sites_by_country(country,final_url)


def create_directory():
    if not os.path.isdir(path):
        os.makedirs(path)


if __name__ == "__main__":

    init_args()
    if b:
        by_countries()
    else:
        global_search()
