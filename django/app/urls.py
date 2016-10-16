"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # base page
    url(r'^$', views.home, name='home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^privacy/', views.privacy, name='privacy'),
    url(r'^contacts/', views.contacts, name='contacts'),
    
    # modules urls
    url(r'^accounts/', include('accounts.urls')),
    url(r'^team/', include('team.urls')),
    url(r'^game/', include('game.urls')),
    url(r'^captcha/', include('captcha.urls')),
]


# settings for development environment DEBUG
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
# if settings.DEBUG:
#     urlpatterns += [
#         url((r'^media/(?P<path>.*)','django.views.static', {'document_root': settings.MEDIA_ROOT}),'serve')
#     ]
    