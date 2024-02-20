from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("reports/", views.reports, name="reports"),
    path("loginpage/", views.loginpage, name="loginpage"),
    path("logoutuser/", views.logoutuser, name="logoutuser"),
    path("usercreation/", views.usercreation, name="user_creation"),
    path("user/", views.userPage, name="user_page"),
    path('createaccount/', views.createaccount, name="createaccount"),
    path('updateaccount/<str:pk>/', views.updateaccount, name="update_account"),
    path("reportusers/", views.reportusers, name="report_user"),
    path("newreport/", views.newreport, name="new_report"),
    path("updatereport/<str:pk>", views.updatereport, name="update_report"),
    path("deletereport/<str:pk>", views.deletereport, name="delete_report"),
    path("userprofile/<str:pk>/", views.userprofile, name="profile"),
   
]