"""
from django.urls import path
from django.conf.urls import url
from . import views

from .views import SignUpView

app_name = 'userprofile'
urlpatterns = [
    path('signup/', views.SignUpView, name='signup'),
    path('profile/<int:pk>', views.get_user_profile, name='user-info'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.view_user_profile, name='author-info'),
    url(r'^profile/edit/$', views.edit_user, name='profile-update'),
]

"""