from django.urls import path, include
from accounts import views

urlpatterns =[


    path("Signup/",views.signup,name="Signup"),
    path("Login/",views.Login,name="Login"),
    path("Logout/",views.Logout,name="Logout"),


]
