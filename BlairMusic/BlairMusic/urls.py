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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from clientesapp import views as cv
from users import views as us
from pdf_convert import views as pdfv
from django.conf import settings
from django.conf.urls.static import static

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

    path('register/', us.register, name="register"),
    path('profile/', us.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name="logout"),
    # path('orden/<int:client_id>', cv.orden, name="orden"),
    # path('orden/<int:client_id>/<int:id>', cv.orden, name="orden"),
    path('vdatein', cv.vdatein, name="vdatein"),
    path('vdateout', cv.vdateout, name="vdateout"),
    path('vprocess/<int:reference_id>', cv.vprocess, name="vprocess"),
    path('varticles/<int:referencia_id>', cv.varticles, name="varticles"),
    path('informes', cv.informes, name="informes"),
    #path('showinfo/<int:id>', pdfv.showinfo, name="showinfo"),
    path('pdf_create/<int:id>', pdfv.pdf_create, name="pdf_create"),
    path('excel_create/<int:id>', pdfv.excel_create, name="excel_create"),
    path('load_images/<int:ref_guia_id>', cv.load_images, name="load_images"),

    path('', include("django.contrib.auth.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)