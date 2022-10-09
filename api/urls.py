from django.urls import path
from . import view

urlpatterns = [
    path('users/', view.getData),
    path('users/post', view.postData),
    path('users/auth', view.authUser),
    path('location/post', view.postLocation)
]