from django.urls import path
from .views import *
urlpatterns = [
    path('',login,name="login"),
    path('register/ ',signup,name="signup"),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('reset-password/', reset_password, name='reset_password'),
    path('administrator/',administrator,name="administrator"),
    path('farmer/',farmer,name="farmer"),
    path('home/',home,name="home"),
    path('profile/',profile,name="profile"),
    path('user/',user,name="user"),
    path('weather/',weathertest,name="weather"),
    # path('weather/', weather_view, name='weather'),
    # path('weather-api/<str:area>/', weather_api, name='weather-api'),
    path('translate_text/',translate_text, name='translate_text')

]
