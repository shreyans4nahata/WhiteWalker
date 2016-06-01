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
from django.http import HttpResponseRedirect
import json
from django.shortcuts import render_to_response

def fetchit(request):
    try:
        print("song fetch called")
        url ="http://www.officialcharts.com/charts/uk-top-40-singles-chart/"
        r= requests.get(url)
        so = BeautifulSoup(r.content,"html.parser")
        l=so.find_all("div", {"class" :"title-artist" })
        l1 = so.find_all("div", {"class" :"cover" })
        gaana=[]
        artist=[]
        nayi=[]
        for k in l:
            gaa,art=(k.get_text().split("\n\n\n"))
            art,som=art.split("\n\n")
            gaana.append(gaa.strip("\n\n"))
            artist.append(art)
            cover=[]
        for k in l1:
            cov=(k.find("img").get("src"))
            cover.append(cov)
        lst=[]
        context_dict = {'gaana':gaana, 'artist':artist,'cover':cover}
        response = render(request,'index.html', context_dict)
        return response

    except Exception as e:
        print(e)
        pass

def sumreq(request):
    try:
        # call("rm -rf static/*m4a")
        # call("rm -rf static/*mp4")
        d=''
        print("func started")
        x=request.GET.get('search','')
        k=request.GET.get('aorv','')
        if k=='a':
            new_query= x + " song only "
            ty= "140"
        else:
            new_query= x +" "
            ty= "18"
       
        url = 'http://www.youtube.com/results?'
        args = {'search_query':new_query}
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
        call(["youtube-dl","-f",ty,"-o",time,final])
        if ty =="140":
            filepath="../../WhiteWalker/mytest/static/*m4a"
        else :
            filepath="../../WhiteWalker/mytest/static/*mp4"
    
        
        y=glob.glob(filepath)
        print(y)     
        for d in y:
            print(d)
            
            if time1 in d:
                print(time1)
                response = HttpResponse()
                fsock = open(d,'rb').read()
                response = HttpResponse(fsock, content_type='audio/mpeg/video')
                if ty =="140":
                    filename = x.strip(" ") + ".m4a" 
                else:
                    filename = x.strip(" ") + ".mp4"

                response['Content-Disposition'] = "attachement; filename=%s" % filename  
                response['Content-Length'] = os.stat(d).st_size
                return response
    except Exception as e:
        print(e)
        pass
