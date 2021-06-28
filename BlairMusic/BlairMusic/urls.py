"""BlairMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from clientesapp import views as cv
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', cv.home, name="home"),
    path('', cv.home, name="home"),
    path('clientesindex/', cv.clientesindex, name="clientesindex"),
    path('clnt/', cv.clnt, name="clform"),
    path('view/', cv.view),
    path('clientepag/<int:id>', cv.clientepag, name="clientepag"),
    path('edit/<int:id>', cv.edit, name="cledit"),
    path('delete/<int:id>', cv.delete),
    path('update/<int:id>', cv.update, name="clupdate"),
    path('ordenindex/', cv.ordenindex, name="ordenindex"),
    path('orderforclient/', cv.orderforclient, name="orderforclient"),
    path('ordenfill/<int:client_id>', cv.ordenfill, name="ordenfill"),
    path('ordenview/<int:id>', cv.ordenview, name="ordenview"),
    path('ordenupd/<int:id>', cv.ordenupd, name="ordenupd"),
    path('ordenmod/<int:id>', cv.ordenmod, name="ordenmod"),
    path('register/', v.register, name="register"),
    path('orden/<int:client_id>', cv.orden, name="orden"),
    path('orden/<int:client_id>/<int:id>', cv.orden, name="orden"),
    path('vdatein', cv.vdatein, name="vdatein"),
    path('', include("django.contrib.auth.urls")),
]
