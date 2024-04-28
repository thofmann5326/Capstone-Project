from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Importing Pygments stuff for syntax highlighting
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Define your models here

class Customer(models.Model):
    # Model representing a customer
    name = models.CharField(max_length=255)  # Customer's name
    # Primary location of the customer
    primary_location = models.CharField(max_length=255)
    # ID of the alignment engineer associated with the customer
    alignment_engineer = models.IntegerField()
    vcio = models.IntegerField()  # ID of the VCIO associated with the customer


class User(models.Model):
    # Model representing a user
    name = models.CharField(max_length=255)  # User's name
    email_address = models.EmailField()  # User's email address
    # Security group the user belongs to
    security_group = models.CharField(max_length=255)


class Project(models.Model):
    # Model representing a project
    name = models.CharField(max_length=255)  # Project name
    status = models.CharField(max_length=255)  # Project status
    project_manager = models.IntegerField()  # ID of the project manager
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Project cost
    description = models.TextField()  # Project description
    completion_date = models.DateField()  # Project completion date


class ProposedProject(models.Model):
    # Model representing a proposed project
    name = models.CharField(max_length=255)  # Proposed project name
    completion_date = models.DateField()  # Proposed project completion date
    description = models.TextField()  # Proposed project description
    customer = models.IntegerField()  # ID of the associated customer


class Assessment(models.Model):
    # Model representing an assessment
    date = models.DateField()  # Date of the assessment
    score = models.DecimalField(
        max_digits=5, decimal_places=2)  # Assessment score
    # Percentage of assessment completion
    percent_complete = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField()  # Comments for the assessment
    status = models.CharField(max_length=255)  # Assessment status
    # Site location of the assessment
    site_location = models.CharField(max_length=255)
    # ID of the assessment template used
    assessment_template = models.IntegerField()
    # ID of the alignment engineer conducting the assessment
    alignment_engineer = models.IntegerField()
    customer = models.IntegerField()  # ID of the associated customer


class AssessmentTemplate(models.Model):
    # Model representing an assessment template
    name = models.CharField(max_length=255)  # Template name
    assessment_type = models.CharField(max_length=255)  # Type of assessment
    description = models.TextField()  # Description of the assessment template


class AssessmentQuestion(models.Model):
    # Model representing an assessment question
    question = models.TextField()  # Assessment question
    answer = models.TextField()  # Answer to the assessment question
    support = models.TextField()  # Additional support for the assessment question


class Recommendation(models.Model):
    # Model representing a recommendation
    name = models.CharField(max_length=255)  # Recommendation name
    completion_date = models.DateField()  # Recommendation completion date
    description = models.TextField()  # Recommendation description
    status = models.CharField(max_length=255)  # Recommendation status
    priority = models.IntegerField()  # Recommendation priority
    assessment = models.IntegerField()  # ID of the associated assessment
    customer = models.IntegerField()  # ID of the associated customer


class RecommendationProposedProject(models.Model):
    # Model representing a recommended proposed project
    recommendation = models.IntegerField()  # ID of the associated recommendation
    # ID of the associated proposed project
    proposed_project = models.IntegerField()


class TechnologyInventory(models.Model):
    # Model representing technology inventory
    device_name = models.CharField(max_length=255)  # Name of the device
    site_location = models.CharField(max_length=255)  # Location of the device
    type = models.CharField(max_length=255)  # Type of the device
    make = models.CharField(max_length=255)  # Make of the device
    model = models.CharField(max_length=255)  # Model of the device
    serial_number = models.CharField(
        max_length=255)  # Serial number of the device
    operating_system = models.CharField(
        max_length=255)  # Operating system of the device
    date_purchased = models.DateField()  # Date when the device was purchased
    # Date when the device's warranty expired
    date_warranty_expired = models.DateField()
    age_years = models.IntegerField()  # Age of the device in years
    # Date when the device information was last updated
    date_last_updated = models.DateField()
    customer = models.IntegerField()  # ID of the associated customer
