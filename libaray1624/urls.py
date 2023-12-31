"""
URL configuration for libaray1624 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views as mv#匯入函式 也可以打成 form mysite.views import homepage

urlpatterns = [ #多打哪個網址會跑去哪
    path('admin/', admin.site.urls),#代表在網址後面打 admin會跑出啥
    path('',mv.homepage,name="homepage"),#網址啥都不打就先連到homepage這裡  如果上面import的方法改成備註的那樣 那這邊的逗號後面打homepage
    path('post/<slug:slug>/', mv.showpost, name="showpost")#slug代表是變數(用<內容就是你在資料庫打的網址名稱>)  如果輸入post/.../就跑去那個函式
]
