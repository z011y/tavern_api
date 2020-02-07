from django.contrib.auth.models import User
from .models import Venue
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .venueSerializers import VenueSerializer
from .userSerializers import UserSerializer, UserSerializerWithToken
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from functools import reduce
from operator import or_


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VenueDetail(generics.ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']
    search_fields = ['slug']

    def get_queryset(self):
        queryset = Venue.objects.all()
        name = self.request.query_params.get('name', None)
        return Venue.objects.filter(name=name)

class VenueList(generics.ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer



@api_view(['GET'])
def current_user(request):

    # Determine the current user by their token, and return their data


    serializer = UserSerializer(request.user)
    return Response(serializer.data)
