from src.celery import app

from datetime import timedelta

from django.utils import timezone

from validate_docbr import CPF

from core.models.proposal import Proposal

cpf = CPF()

@app.task(bind=True)
def process_proposals(self):
    """
    Process all proposals with status "pending" and change the status to "accepted" or "declined" or "expired"
    """
    proposals = Proposal.objects.filter(status="pending")
    for proposal in proposals:
        try:
            proposal_time_limit = proposal.created_at + timedelta(minutes=5)
            if proposal_time_limit < timezone.now():
                proposal.status = "expired"
                proposal.save()
                print(f"Proposal id: {proposal.id} - Status: {proposal.status}")
                continue

            document_is_valid = cpf.validate(proposal.document)

            print(document_is_valid)

            if document_is_valid and proposal.proposal_value >= 1000:
                proposal.status = "accepted"
                proposal.save()
                print(f"Proposal id: {proposal.id} - Status: {proposal.status}")
                continue
            else:
                proposal.status = "declined"
                proposal.save()
                print(f"Proposal id: {proposal.id} - Status: {proposal.status}")
                continue
        except Exception as e:
            print(e)
            continue
    return True
