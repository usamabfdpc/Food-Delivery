from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('homepage',views.HomePage.as_view(),name="homepage"),
     path('registration',views.Registration.as_view(),name='register'),
]
