from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from polls import views

urlpatterns = patterns('',
    #url(r'^/top',views.fetchit, name='fetchit'),
    url(r'^$',views.sumreq,name='sumreq'),
    #url(r'^$',views.fetchit, name='fetchit' ),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
