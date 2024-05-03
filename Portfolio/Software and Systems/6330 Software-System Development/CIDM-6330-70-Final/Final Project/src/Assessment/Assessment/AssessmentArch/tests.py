from django.test import TestCase
from django.utils.timezone import localtime
from AssessmentAPI.models import Assessment
from AssessmentArch.services.commands import (
    AddAssessmentCommand,
    ListAssessmentsCommand,
    DeleteAssessmentCommand,
    UpdateAssessmentCommand,
)


class TestCommands(TestCase):
    def setUp(self):
        self.timestamp = localtime().isoformat()
        self.assessment_data = {
            'date': self.timestamp,
            'score': 95.5,
            'percent_complete': 100.0,
            'comments': 'Test comments',
            'status': 'Completed',
            'site_location': 'Test location',
        }

    def test_command_add(self):
        add_command = AddAssessmentCommand()
        add_command.execute(data=self.assessment_data)
        self.assertEqual(Assessment.objects.count(), 1)
        added_assessment = Assessment.objects.first()
        self.assertEqual(added_assessment.date, self.timestamp)
        self.assertEqual(added_assessment.score, 95.5)
        self.assertEqual(added_assessment.percent_complete, 100.0)
        self.assertEqual(added_assessment.comments, 'Test comments')
        self.assertEqual(added_assessment.status, 'Completed')
        self.assertEqual(added_assessment.site_location, 'Test location')

    def test_command_list(self):
        add_command = AddAssessmentCommand()
        add_command.execute(data=self.assessment_data)
        list_command = ListAssessmentsCommand()
        assessments = list_command.execute()
        self.assertEqual(len(assessments), 1)

    def test_command_delete(self):
        add_command = AddAssessmentCommand()
        add_command.execute(data=self.assessment_data)
        delete_command = DeleteAssessmentCommand()
        delete_command.execute(data={'id': 1})
        self.assertEqual(Assessment.objects.count(), 0)

    def test_command_update(self):
        add_command = AddAssessmentCommand()
        add_command.execute(data=self.assessment_data)
        update_command = UpdateAssessmentCommand()
        updated_data = {
            'id': 1,
            'score': 90.0,
            'status': 'In Progress',
        }
        update_command.execute(data=updated_data)
        updated_assessment = Assessment.objects.get(id=1)
        self.assertEqual(updated_assessment.score, 90.0)
        self.assertEqual(updated_assessment.status, 'In Progress')
