from .views import Venue
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = ('venue_id', 'name', 'email', 'phone', 'address', 'img', 'slug')
