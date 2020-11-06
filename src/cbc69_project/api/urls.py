from django.conf.urls import url, include

from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('tournament', views.TournamentViewSet)
router.register('post', views.PostViewSet)
router.register('volunteering', views.VolunteeringViewSet)
router.register('interclub teams', views.InterclubTeamViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^token/', auth_views.obtain_auth_token),
]
