"""
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
"""
import sys
from abc import ABC, abstractmethod
from datetime import datetime
from injector import Injector, inject
import pytz

import requests
from django.db import transaction

from AssessmentAPI.models import Assessment
from AssessmentArch.domain.model import DomainAssessment


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError(
            "A command must implement the execute method")


class PythonTimeStampProvider:
    def __init__(self):
        self.now = datetime.now(pytz.UTC).isoformat()


class AddAssessmentCommand(Command):
    """
    Add an assessment to the database.
    """

    @inject
    def __init__(self, now: PythonTimeStampProvider = PythonTimeStampProvider()):
        self.now = now

    def execute(self, data: dict, timestamp=None):
        assessment = Assessment(**data)
        assessment.date = timestamp or self.now

        # Use Django's transaction management
        with transaction.atomic():
            assessment.save()


class ListAssessmentsCommand(Command):
    """
    Retrieve a list of assessments from the database.
    """

    def __init__(self, order_by="date"):
        self.order_by = order_by

    def execute(self, data=None):
        return Assessment.objects.all().order_by(self.order_by)


class DeleteAssessmentCommand(Command):
    """
    Delete an assessment from the database.
    """

    def execute(self, data: dict):
        assessment = Assessment.objects.get(id=data['id'])
        with transaction.atomic():
            assessment.delete()


class UpdateAssessmentCommand(Command):
    """
    Update an assessment in the database.
    """

    def execute(self, data: dict):
        assessment = Assessment.objects.get(id=data['id'])
        for key, value in data.items():
            setattr(assessment, key, value)
        with transaction.atomic():
            assessment.save()
