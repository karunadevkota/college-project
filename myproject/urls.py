from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('register/',views.register,name="register"),
    path('check_user_exists/',views.check_user_exists,name="check_user_exist"),
    path('login/',views.signin,name='login'),
    path('report/',views.report,name='report'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('news/',views.news,name='news'),
    path('emergencycontact/',views.econtact,name='econtact'),
    path('policestation/',views.station,name='station'),
    path('record/',views.record,name='record'),
    
   
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)