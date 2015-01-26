from __future__ import unicode_literals
from subprocess import call
from django.views.static import serve
from django.shortcuts import get_object_or_404
import glob
import os
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpRequest
import urllib.request
import requests
from bs4 import BeautifulSoup
import youtube_dl
def sumreq(request):
    print("func started")
    x=request.GET.get('srch','')        
    url = 'http://www.youtube.com/results?'
    args = {'search_query':x}
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
    time = datetime.datetime.now().strftime("%I%M%p%B%d%Y")
    time+="aaaaaa"
    time+=".m4a"
    print(time)
    call(["youtube-dl","-f","141","-o",time,final])
    filepath="C:/Python34/Scripts/mytest/*m4a"
    y=glob.glob(filepath)
    for a in y:
        for time in a:
            response =HttpResponse(a)
            return response
    