"""record URL Configuration

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

from django.conf.urls import url, include
from django.contrib import admin
from upload import views as up_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^paint/$',up_views.paint_board,name='paint'),
    url(r'^upload/$', up_views.upload_file,name='upload'),
    url(r'^pdf/$',up_views.pdf_play,name='pdf'),
    url(r'^lead/$',up_views.leadpage,name='lead'),
]

# upload app
#urlpatterns += upload_urls.urlpatterns
#name作用是在ｈｔｍｌ中增加路由可以使用　｛％　ｕｒｌ　‘ｎａｍｅ’　％｝访问其他的ｕｒｌ

