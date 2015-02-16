from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from polls import views

urlpatterns = patterns('',
    url(r'^$',views.sumreq,name='sumreq'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
