from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

from . import serializers, models


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

class TournamentViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating tournaments."""

    serializer_class = serializers.TournamentSerializer
    queryset = models.Tournament.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating posts."""

    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()

class VolunteeringViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating volunteering events."""

    serializer_class = serializers.VolunteeringSerializer
    queryset = models.Volunteering.objects.all()

class InterclubTeamViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating interclub teams."""

    serializer_class = serializers.InterclubTeamSerializer
    queryset = models.InterclubTeam.objects.all()

