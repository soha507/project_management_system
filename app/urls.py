from django.urls import path
from . import views
urlpatterns =[# path('admin/', admin.site.urls),
              path('home/',views.index,name='index' ),
              path('about/', views.about, name='about'),
              path('appointment/', views.appointment1, name='appointment'),
              path('contact/', views.contact, name='contact'),
              path('service/', views.service, name='service'),
              path('history/', views.history, name='history'),
              path('', views.login, name='login'),
              path('login/', views.login, name='login'),
              path('registration/', views.registration, name='registration'),
              path('loginout/', views.loginout, name='logout'),
              path('fp/', views.fp, name="Forgot Password"),
              path('fp1/', views.fp1, name="Fp1"),
              path('cp/', views.cp, name="Change Password"),
              path('cp1/', views.cp1, name="Changing password")


]