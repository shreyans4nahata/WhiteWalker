from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic import TemplateView
from polls import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$',views.sumreq,name='sumreq'),
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    #url(r'^$',views.index, name= 'index'),
    
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    #url(r'^$',views.index, name= 'index'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
