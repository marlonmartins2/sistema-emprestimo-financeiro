from rest_framework import viewsets

from core.models import Proposal

from core.api.serializers import ProposalSerializer


class ProposalViewSet(viewsets.ModelViewSet):
    """
    Proposal model view set.
    :param viewsets.ModelViewSet: The base viewset.
    :type viewsets.ModelViewSet: viewsets.ModelViewSet
    """

    #: serializers.ModelSerializer: The Proposal serializer.
    serializer_class = ProposalSerializer

    #: queryset: The Proposal model queryset.
    queryset = Proposal.objects.all()
