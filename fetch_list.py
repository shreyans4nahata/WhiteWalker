from __future__ import unicode_literals
import urllib.request
import requests
from bs4 import BeautifulSoup
from json import JSONEncoder
url ="http://www.officialcharts.com/charts/uk-top-40-singles-chart/"
r= requests.get(url)
so = BeautifulSoup(r.content,"html.parser")
l=so.find_all("div", {"class" :"title-artist" })
l1 = so.find_all("div", {"class" :"cover" })
gaana=[]
artist=[]
for k in l:
    gaa,art=(k.get_text().split("\n\n\n"))
    art,som=art.split("\n\n")
    gaana.append(gaa.strip("\n\n"))
    artist.append(art)
cover=[]
for k in l1:
    cov=(k.find("img").get("src"))
    cover.append(cov)
d={}
lst=[]
for i in range(0,40):
    d[i] = {'gaana':gaana[i],'artist':artist[i],'cover':cover[i]}    
print(d)
print(type(d[0]))
