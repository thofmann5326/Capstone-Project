import asyncio
import datetime
import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync

from .models import Assessment, TechnologyInventory

# Consumer for printing simple assessment events


class SimpleAssessmentConsumer(AsyncJsonWebsocketConsumer):
    async def print_assessment(self, event):
        # Print assessment data received from event
        print(f"WORKER: Assessment: {event['data']}")

# Consumer for handling assessment-related WebSocket interactions


class AssessmentConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # Accept connection
        await self.accept()

    async def receive_json(self, content):
        # Handle incoming JSON messages (if needed)
        pass

    async def disconnect(self, close_code):
        # Handle WebSocket disconnect
        pass

    async def handle(self, body):
        # Retrieve all assessments from the database
        assessments = Assessment.objects.all()

        # Prepare assessment data for sending
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

        # Send assessment data as JSON to the WebSocket
        await self.send_json(data)

    async def send_assessment(self, assessment):
        # Prepare assessment data for sending
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

        # Send assessment data to the 'assessments' group
        await self.channel_layer.group_send(
            "assessments", {"type": "send.assessment", "data": data}
        )

# Consumer for printing technology inventory events


class TechnologyInventoryConsumer(AsyncJsonWebsocketConsumer):
    async def print_technology_inventory(self, event):
        # Print technology inventory data received from event
        print(f"WORKER: Technology Inventory: {event['data']}")
