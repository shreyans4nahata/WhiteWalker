<<<<<<< HEAD
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from django.conf.urls.static import static
from django.views.generic import TemplateView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    (r'^$',TemplateView.as_view(template_name="index.html")),
    (r'^index.html',TemplateView.as_view(template_name="index.html")),
=======
=======
from django.conf.urls import patterns, include, url
from django.contrib import admin
>>>>>>> b189e1514c848c9ee5dfcf7cbe9bd1d48e4080bb
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^$',TemplateView.as_view(template_name="index.html")),
    url(r'^index.html',TemplateView.as_view(template_name="index.html")),
>>>>>>> server updated once again
=======
    url(r'^$',TemplateView.as_view(template_name="urlost.html")),
    url(r'^index.html',TemplateView.as_view(template_name="index.html")),
>>>>>>> b189e1514c848c9ee5dfcf7cbe9bd1d48e4080bb
    url(r'^polls/',include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
