import csv
from pathlib import Path

from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Customer, Project, ProposedProject, Assessment, RecommendationProposedProject, TechnologyInventory
file_path = Path(__file__).parent.parent / "Assessment" / \
    "AssessmentAPI" / "created_log.csv"


@receiver(post_save, sender=Assessment)
def log_assessment_to_csv(sender, instance, created, **kwargs):
    if created:
        print("Assessment signal: CSV")
        print(f"Writing to {file_path}")

        with open(file_path, "a+", newline="") as csvfile:
            logfile = File(csvfile)
            logwriter = csv.writer(
                logfile,
                delimiter=",",
            )
            logwriter.writerow(
                [
                    instance.date,
                    instance.score,
                    instance.percent_complete,
                    instance.comments,
                    instance.status,
                    instance.site_location,
                    instance.assessment_template_id,
                    instance.alignment_engineer_id,
                    instance.customer_id,
                ]
            )


@receiver(post_save, sender=TechnologyInventory)
def send_technology_inventory_to_channel(sender, instance, created, **kwargs):
    if created:
        print("Technology Inventory signal: Channel")
        print(f"Sending technology inventory to channel: {instance}")

        async_to_sync(channel_layer.send)(
            "technology-inventory-add", {
                "type": "print.technology_inventory", "data": instance.device_name}
        )


post_save.connect(log_assessment_to_csv, sender=Assessment)
post_save.connect(send_technology_inventory_to_channel,
                  sender=TechnologyInventory)
