from __future__ import unicode_literals
from subprocess import call
from django.views.static import serve
from django.shortcuts import get_object_or_404
from timeout import timeout
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
    try:

        #response=''
        d=''
        print("func started")
        x=request.GET.get('search','')        
        if x == '' :
            return
        url = 'http://www.youtube.com/results?'
        args = {'search_query':x}
        r = requests.get(url,params=args)
        so=BeautifulSoup(r.content)
        l=so.find_all("h3", {"class" :"yt-lockup-title" })
        k=[]
        k.append(str(l[0]).split(" "))
        print(k[0])
        for i in k[0]:
            if 'href' in i :
                s=i
                print(i)
                break
        (a,b,c)=s.split('"')
        print(b)
        final="https://www.youtube.com" + b
        print(final)
        time="./static/"
        time+=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        time+="aaaaaa"
        time+=".%(ext)s"
        time1="/static/"
        time1+=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        time1+="aaaaaa"
        

        print(time)
        call(["youtube-dl","-f","18","-o",time,final])
        filepath="/home/ubuntu/Lanterns/server/WhiteWalker/mytest/static/*m4a"
        y=glob.glob(filepath)
        print(y)     
        for d in y:
            print(d)
            if time in d:
                response = HttpResponse()
                fsock = open(d,'rb').read()
                response = HttpResponse(fsock, content_type='audio/mpeg')
                filename = x.strip(" ") + ".m4a" 
                response['Content-Disposition'] = "attachement; filename=%s" % filename  
                response['Content-Length'] = os.stat(d).st_size
                return response
    except Exception as e:
        print(e)
        pass
