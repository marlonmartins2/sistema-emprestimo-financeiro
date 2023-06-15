from rest_framework import viewsets

from core.models import User

from core.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User model view set.
    :param viewsets.ModelViewSet: The base viewset.
    :type viewsets.ModelViewSet: viewsets.ModelViewSet
    """

    #: serializers.ModelSerializer: The User serializer.
    serializer_class = UserSerializer

    #: queryset: The User model queryset.
    queryset = User.objects.all()
