from rest_framework import serializers

from core.models import Proposal


class ProposalSerializer(serializers.ModelSerializer):
    """
    Proposal model serializer.

    :param serializers.ModelSerializer: The base serializer.
    :type serializers.ModelSerializer: serializers.ModelSerializer
    """

    class Meta:
        """
        Meta class for the proposal model serializer.
        """

        #: model: The model to serialize.
        model = Proposal

        #: fields: The fields to serialize.
        fields = [
            "id",
            "full_name",
            "document",
            "address",
            "proposal_value",
            "status",
            "created_at",
        ]
        extra_kwargs = {
            "status": {"read_only": True},
            "created_at": {"read_only": True},
        }
