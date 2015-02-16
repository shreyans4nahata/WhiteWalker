from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$',TemplateView.as_view(template_name="index.html")),
    url(r'^index.html',TemplateView.as_view(template_name="index.html")),
    url(r'^polls/',include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
