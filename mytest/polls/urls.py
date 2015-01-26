from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', views.index,name='index'),
    url(r'^$',views.sumreq,name='sumreq'),
)
