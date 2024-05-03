from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Customer, User, Project, ProposedProject, Assessment, AssessmentTemplate, AssessmentQuestion, Recommendation, RecommendationProposedProject, TechnologyInventory


class AssessmentsTests(APITestCase):
    def test_create_customer(self):
        vcio = User.objects.create(
            name="vCIO User",
            email_address="vcio@example.com",
            security_group="vcio_group"
        )

        return Customer.objects.create(
            name="Example Customer",
            primary_location="Example Location",
            alignment_engineer_id=1,
            vcio_id=vcio.id
        )

    def test_create_user(self):
        return User.objects.create(
            name="Example User",
            email_address="example@example.com",
            security_group="example_group"
        )

    def test_create_project(self):
        # Using the previously defined test method
        project_manager = self.test_create_user()
        return Project.objects.create(
            name="Example Project",
            status="Example Status",
            project_manager=project_manager,  # Pass the user object directly
            cost=1000.00,
            description="Example Description",
            customer=self.test_create_customer(),  # Creating a customer for the project
            completion_date="2024-04-23"
        )

    def test_create_proposed_project(self):
        return ProposedProject.objects.create(
            name="Example Proposed Project",
            completion_date="2024-04-23",
            description="Example Description",
            # Creating a customer for the proposed project
            customer=self.test_create_customer()
        )

    def test_create_assessment_template(self):
        return AssessmentTemplate.objects.create(
            name="Example Template",
            assessment_type="Example Type",
            description="Example Description"
        )

    def test_create_assessment_question(self):
        return AssessmentQuestion.objects.create(
            question="Example Question",
            answer="Example Answer",
            support="Example Support"
        )

    def test_create_assessment(self):
        user = self.test_create_user()
        customer = self.test_create_customer()
        assessment_template = self.test_create_assessment_template()

        return Assessment.objects.create(
            date="2024-04-23",
            score=95.5,
            percent_complete=100.0,
            comments="Example Comments",
            status="Completed",
            site_location="Example Location",
            assessment_template=assessment_template,
            alignment_engineer=user,
            customer=customer
        )

    def test_create_recommendation_proposed_project(self):
        recommendation = Recommendation.objects.create(
            name="Example Recommendation",
            completion_date="2024-04-23",
            description="Example Description",
            status="Completed",
            priority=10,
            # Creating an assessment for the recommendation
            assessment=self.test_create_assessment(),
            # Creating a customer for the recommendation
            customer=self.test_create_customer()
        )

        # Creating a proposed project for the recommendation
        proposed_project = self.test_create_proposed_project()

        return RecommendationProposedProject.objects.create(
            recommendation=recommendation,
            proposed_project=proposed_project
        )

    def test_create_technology_inventory(self):
        """
        Ensure we can create a new technology inventory object.
        """
        # Create a customer object first
        customer = self.test_create_customer()

        # Create the technology inventory object
        return TechnologyInventory.objects.create(
            device_name="Example Device",
            site_location="Example Location",
            type="Example Type",
            make="Example Make",
            model="Example Model",
            serial_number="Example Serial",
            operating_system="Example OS",
            date_purchased="2024-04-23",
            date_warranty_expired="2025-04-23",
            age_years=1,
            date_last_updated="2024-04-23",
            customer=customer
        )
