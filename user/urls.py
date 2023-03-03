from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signup/email/', views.signupwithemail, name='signupwithemail'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('settings/profile/', views.edit, name='edit_profile'),
    path('akjbfalsdfakjsdgfsdgkashdfkjahsdlfjasdfhkajsdfkjasgdfkaglsdgjgalsdflsdsfasd/follow/', views.follow, name='follow'),
]
