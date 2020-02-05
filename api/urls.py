from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views



from django.urls import path
from .views import current_user, UserList, VenueList, VenueDetail

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('venues/', VenueList.as_view()),
    path('venue_detail/', VenueDetail.as_view())
]
