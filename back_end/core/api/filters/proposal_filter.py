import django_filters as filters

from core.models.proposal import Proposal


class ProposalFilter(filters.FilterSet):
    """
    Filter for Proposal model
    """

    class Meta:
        """
        Class Meta for ProposalFilter
        """

        #: filters.CharFilter: The status filter.
        status = filters.CharFilter(field_name="status")

        #: filters.CharFilter: The document filter.
        document = filters.CharFilter(field_name="document")

        #: filters.NumberFilter: The proposal_value filter.
        proposal_value = filters.NumberFilter(field_name="proposal_value")

        #: models.Model: The proposal model.
        model = Proposal

        #: list: The fields to be filtered.
        fields = {
            "status": ["exact"],
            "document": ["exact"],
            "proposal_value": ["exact"],
        }
