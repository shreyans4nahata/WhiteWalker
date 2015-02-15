from django.conf.urls import patterns, url
<<<<<<< HEAD
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
from django.views.generic import TemplateView
>>>>>>> server updated once again
=======
from django.views.generic import TemplateView
>>>>>>> b189e1514c848c9ee5dfcf7cbe9bd1d48e4080bb
from polls import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$',views.sumreq,name='sumreq'),
<<<<<<< HEAD
<<<<<<< HEAD
=======
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    #url(r'^$',views.index, name= 'index'),
    
>>>>>>> server updated once again
=======
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    #url(r'^$',views.index, name= 'index'),
    
>>>>>>> b189e1514c848c9ee5dfcf7cbe9bd1d48e4080bb
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
