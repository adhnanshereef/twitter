from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signup/email/', views.signupwithemail, name='signupwithemail'),
    path('logout/', views.signout, name='logout'),
]
