from django.urls import include, path

from rest_framework import routers

from core.api import viewsets


router = routers.DefaultRouter()

router.register(r"proposals", viewsets.ProposalViewSet, basename="proposals")
router.register(r"user", viewsets.UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]