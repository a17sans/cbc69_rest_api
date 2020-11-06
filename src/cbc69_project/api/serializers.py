from rest_framework import serializers, fields

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our profile object."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'lastname', 'firstname', 'license_number','last_login', 'password')
        extra_kwargs = {
            'last_login': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Used to create a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            lastname=validated_data['lastname'],
            firstname=validated_data['firstname'],
            license_number=validated_data['license_number']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class TournamentSerializer(serializers.ModelSerializer):
    """A serializer for our tournament object."""

    class Meta:
        model = models.Tournament
        fields=('__all__')

class PostSerializer(serializers.ModelSerializer):
    """A serializer for our posts objects."""

    class Meta:
        model = models.Post
        fields = ('__all__')

class VolunteeringSerializer(serializers.ModelSerializer):
    """A serializer for our volunteering events."""

    class Meta:
        model = models.Volunteering
        fields = ('__all__')

class InterclubTeamSerializer(serializers.ModelSerializer):
    """A serializer for our interclub teams."""

    class Meta:
        model = models.InterclubTeam
        fields = ('__all__')