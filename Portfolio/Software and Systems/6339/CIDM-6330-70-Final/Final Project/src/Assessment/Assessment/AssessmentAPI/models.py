from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# from barkyarch.domain.model import DomainBookmark

# pygments stuff
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255)
    primary_location = models.CharField(max_length=255)
    alignment_engineer = models.ForeignKey(
        'User', related_name='alignment_engineered_customers', on_delete=models.CASCADE)
    vcio = models.ForeignKey(
        'User', related_name='vcio_customers', on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.EmailField()
    security_group = models.CharField(max_length=255)


class Project(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    project_manager = models.ForeignKey('User', on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    completion_date = models.DateField()


class ProposedProject(models.Model):
    name = models.CharField(max_length=255)
    completion_date = models.DateField()
    description = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Assessment(models.Model):
    date = models.DateField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    percent_complete = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField()
    status = models.CharField(max_length=255)
    site_location = models.CharField(max_length=255)
    assessment_template = models.ForeignKey(
        'AssessmentTemplate', on_delete=models.CASCADE)
    alignment_engineer = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class AssessmentTemplate(models.Model):
    name = models.CharField(max_length=255)
    assessment_type = models.CharField(max_length=255)
    description = models.TextField()


class AssessmentQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    support = models.TextField()


class Recommendation(models.Model):
    name = models.CharField(max_length=255)
    completion_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=255)
    priority = models.IntegerField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class RecommendationProposedProject(models.Model):
    recommendation = models.ForeignKey(
        Recommendation, on_delete=models.CASCADE)
    proposed_project = models.ForeignKey(
        ProposedProject, on_delete=models.CASCADE)


class TechnologyInventory(models.Model):
    device_name = models.CharField(max_length=255)
    site_location = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    operating_system = models.CharField(max_length=255)
    date_purchased = models.DateField()
    date_warranty_expired = models.DateField()
    age_years = models.IntegerField()
    date_last_updated = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
