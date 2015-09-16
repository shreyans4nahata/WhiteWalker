from __future__ import unicode_literals
from subprocess import call
import urllib.request
import requests
from bs4 import BeautifulSoup
import youtube_dl
srch=input()
url = 'http://www.youtube.com/results?'
args = {'search_query':srch}
r = requests.get(url,params=args)
so=BeautifulSoup(r.content)
l=so.find_all("h3", {"class" :"yt-lockup-title" })
k=[]
k.append(str(l[0]).split(" "))
for i in k[0]:
    if 'href' in i :
        s=i
        break
(a,b,c)=s.split('"')
final="https://www.youtube.com" + b
print(final)
ydl_opts={}
call(["youtube-dl","-f","141",final])

