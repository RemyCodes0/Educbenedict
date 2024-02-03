from django.urls import path, include
from . import views
app_name = 'authentication'
urlpatterns = [
    path('logins/', views.logins, name = 'logins'),
    path('logout', views.logouts, name = 'logouts'),
    path('signup/', views.signup, name = 'signup')
]

