import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models.base_model import BaseModel



class User(BaseModel, AbstractUser):
    """
    User data model.

    :param core.BaseModel: The base model.
    :type models.Model: Model
    """

    class Meta:
        """
        Meta class for the User data model.
        """

        #: str: The model database name.
        db_table = "users"

        #: str: The model verbose name.
        verbose_name = "User"

        #: str: The model plural verbose name.
        verbose_name_plural = "Users"

    #: models.UUIDField: The user id.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #: models.CharField: The user name.
    username = models.CharField(unique=True, max_length=255)

    #: models.CharField: The user password.
    password = models.CharField(max_length=255)

    #: models.CharField: The document.
    document = models.CharField(max_length=11)

    #: models.BooleanField: The is admin flag.
    is_admin = models.BooleanField(default=False)

    #: models.BooleanField: The is staff flag.
    is_staff = models.BooleanField(default=False)
