from rest_framework import viewsets, filters

from django_filters.rest_framework import DjangoFilterBackend

from core.models import Proposal

from core.api.serializers import ProposalSerializer

from core.api.filters.proposal_filter import ProposalFilter


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

    #: filter_backends: The filter backends.
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    #: ProposalsFilter: The Proposal custom filter.
    filterset_class = ProposalFilter

    #: search_fields: The search fields.
    search_fields = ["status", "document", "proposal_value"]
