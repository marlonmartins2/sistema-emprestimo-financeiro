from django.db import models


class BaseModel(models.Model):
    """
    The base application model.

    :param models.Model: The base model class.
    :type models.Model: models.Model
    """

    #: models.DateTimeField: The model instance creation date.
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        """
        Meta class for the base application model.
        """

        #: bool: If the class is abstract or not.
        abstract = True
