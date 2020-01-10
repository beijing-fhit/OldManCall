"""OldManCall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
# from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include
from django.views.generic import TemplateView
from backend import views

# from OldManCall import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^$', views.index),
    url(r'api/.*', lambda e: HttpResponse('戏说不是胡说')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^code/', views.get_code, name='code'),
    url(r'^openid/', views.get_open_id, name='openid'),
    url(r'^getopenid/', views.get_openid_from_session, name='getopenid'),
    url(r'^scan/', views.scan, name='scan'),
    url(r'^scan_resul/', views.scan_result, name='scan_result'),
    url(r'^qr_code_info/',views.qr_code_info,name='qr_code_info')
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
