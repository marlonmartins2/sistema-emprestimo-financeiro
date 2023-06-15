from uuid import uuid4

from django.db import models

from core.models.base_model import BaseModel


class Proposal(BaseModel):
    """
    Proposal data model.

    :param core.BaseModel: The base model.
    :type models.Model: Model
    """

    class Meta:
        """
        Meta class for the Proposal data model.
        """

        #: str: The model database name.
        db_table = "proposals"

        #: str: The model verbose name.
        verbose_name = "Proposal"

        #: str: The model plural verbose name.
        verbose_name_plural = "Proposals"

    #: models.UUIDField: The primary key for identification.
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    #: models.CharField: The full name of person.
    full_name = models.CharField(max_length=255)

    #: models.CharField: The document of person.
    document = models.CharField(max_length=11)

    #: models.JSONField: The person address.
    address = models.JSONField(null=True, blank=True)

    #: models.DecimalField: The proposal value.
    proposal_value = models.DecimalField(max_digits=10, decimal_places=2)

    #: models.CharField: The proposal status.
    status = models.CharField(
        max_length=10,
        choices=(
            ("pending", "Pending"),
            ("accepted", "Accepted"),
            ("declined", "Declined"),
            ("expired", "Expired"),
        ),
        default="pending",
    )
