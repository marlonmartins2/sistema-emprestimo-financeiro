import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

app = Celery("src")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(["core"])

# Celery Beat Settings

app.conf.beat_schedule = {
    "health_check": {
        "task": "src.celery.health_check",
        "schedule": 5,
    },
    "process_proposals": {
        "task": "core.tasks.process_proposals",
        "schedule": 15,
    },
}

@app.task(bind=True)
def health_check(self):
    return True
