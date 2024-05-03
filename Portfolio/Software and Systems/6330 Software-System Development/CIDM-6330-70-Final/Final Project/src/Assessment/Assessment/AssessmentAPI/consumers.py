import asyncio
import datetime
import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync

from .models import Assessment, TechnologyInventory


class SimpleAssessmentConsumer(AsyncJsonWebsocketConsumer):
    async def print_assessment(self, event):
        print(f"WORKER: Assessment: {event['data']}")


class AssessmentConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive_json(self, content):
        # You can handle incoming JSON messages here if needed
        pass

    async def disconnect(self, close_code):
        pass

    async def handle(self, body):
        assessments = Assessment.objects.all()
        data = [
            {
                "date": assessment.date,
                "score": assessment.score,
                "percent_complete": assessment.percent_complete,
                "comments": assessment.comments,
                "status": assessment.status,
                "site_location": assessment.site_location,
                "assessment_template_id": assessment.assessment_template_id,
                "alignment_engineer_id": assessment.alignment_engineer_id,
                "customer_id": assessment.customer_id,
            }
            for assessment in assessments
        ]
        await self.send_json(data)

    async def send_assessment(self, assessment):
        data = {
            "date": assessment.date,
            "score": assessment.score,
            "percent_complete": assessment.percent_complete,
            "comments": assessment.comments,
            "status": assessment.status,
            "site_location": assessment.site_location,
            "assessment_template_id": assessment.assessment_template_id,
            "alignment_engineer_id": assessment.alignment_engineer_id,
            "customer_id": assessment.customer_id,
        }
        await self.channel_layer.group_send(
            "assessments", {"type": "send.assessment", "data": data}
        )


class TechnologyInventoryConsumer(AsyncJsonWebsocketConsumer):
    async def print_technology_inventory(self, event):
        print(f"WORKER: Technology Inventory: {event['data']}")
