from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [

path('',views.index,name="index" ),
path('register',views.rigi,name="register" ),
path('login',views.login,name="login" ),
path('userhome',views.userhome,name="userhome" ),

path('checklogin',views.checklogin,name="checklogin" ),
path('upload',views.addproduct,name="upload" ),
path('logout',views.logout,name="logout" ),







]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
