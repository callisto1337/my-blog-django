"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('', 
    url(r'^$', views.post_list, name='post_list'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^reg/$', views.reg, name='reg'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
