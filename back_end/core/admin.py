from django.contrib import admin

from core.models import Proposal, User

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    """
    Proposal model admin.
    """
    list_display = ("id", "full_name", "proposal_value", "status", "created_at")

    list_filter = ("status", "created_at", "proposal_value")


# Register your models here.

admin.site.register(User)