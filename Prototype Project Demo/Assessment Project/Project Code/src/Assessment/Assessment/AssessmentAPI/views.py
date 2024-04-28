from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import random
from datetime import datetime, timedelta
from django.db.models import Count
from django.shortcuts import get_object_or_404

# Importing models and serializers from the same app
from .models import Customer, User, Project, ProposedProject, Assessment, AssessmentTemplate, AssessmentQuestion, Recommendation, RecommendationProposedProject, TechnologyInventory
from .serializers import CustomerSerializer, UserSerializer, ProjectSerializer, ProposedProjectSerializer, AssessmentSerializer, AssessmentTemplateSerializer, AssessmentQuestionSerializer, RecommendationSerializer, RecommendationProposedProjectSerializer, TechnologyInventorySerializer


def get_os_counts(request, customer_id):
    # Retrieve the customer object based on the provided customer_id
    customer = 1  # This is a placeholder value; it should be replaced with the actual retrieval logic

    # Assuming TechnologyInventory model has a field 'operating_system' for the operating system
    # Count occurrences of each operating system for the specified customer
    os_counts = TechnologyInventory.objects.filter(customer=customer).values(
        'operating_system').annotate(count=Count('operating_system'))

    # Initialize counts for each operating system to 0
    linux_count = 0
    windows_count = 0
    macos_count = 0

    # Loop through the counts and update respective variables
    for os_count in os_counts:
        if os_count['operating_system'] == 'Linux':
            linux_count = os_count['count']
        elif os_count['operating_system'] == 'Windows':
            windows_count = os_count['count']
        elif os_count['operating_system'] == 'macOS':
            macos_count = os_count['count']

    # Return the counts as JSON response
    return JsonResponse({
        'linuxCount': linux_count,
        'windowsCount': windows_count,
        'macosCount': macos_count
    })


def customer_summary_view(request):
    # Retrieve relevant data
    customer_id = 1  # Assuming you want details for customer with ID 1
    customer = Customer.objects.get(pk=customer_id)  # Fetch customer details

    machine_inventory = TechnologyInventory.objects.filter(
        customer=customer_id)
    assessments = Assessment.objects.filter(customer=customer_id)

    alignment_engineer_id = customer.alignment_engineer
    alignment_engineer = User.objects.get(pk=alignment_engineer_id)
    customer.alignment_engineer = alignment_engineer.name

    vCIO_id = customer.vcio
    vcio = User.objects.get(pk=vCIO_id)
    customer.vcio = vcio.name

    recommendations = Recommendation.objects.filter(customer=customer_id)

    # Calculate counts for warranty status
    under_warranty_count = TechnologyInventory.objects.filter(
        customer=customer_id, age_years__lte=5).count()
    out_of_warranty_count = TechnologyInventory.objects.filter(
        customer=customer_id, age_years__gt=5).count()

    # Calculate counts for operating systems
    linux_count = TechnologyInventory.objects.filter(
        customer=customer_id, operating_system='Linux').count()
    windows_count = TechnologyInventory.objects.filter(
        customer=customer_id, operating_system='Windows').count()
    macos_count = TechnologyInventory.objects.filter(
        customer=customer_id, operating_system='MacOS').count()

    # Pass data to the template
    context = {
        'machine_inventory': machine_inventory,
        'assessments': assessments,
        'recommendations': recommendations,
        'customer': customer,
        'under_warranty_count': under_warranty_count,
        'out_of_warranty_count': out_of_warranty_count,
        'linux_count': linux_count,
        'windows_count': windows_count,
        'macos_count': macos_count,
    }

    return render(request, 'customer_summary.html', context)


def assessment_edit_view(request, assessment_id):
    customer = 1  # Placeholder value; replace with actual logic to retrieve customer
    assessments = Assessment.objects.filter(customer=customer)

    alignment_engineer_names = {}
    for assessment in assessments:
        alignment_engineer_id = assessment.alignment_engineer
        alignment_engineer = User.objects.get(pk=alignment_engineer_id)
        assessment.alignment_engineer = alignment_engineer.name

    context = {
        'assessments': assessments,
        'alignment_engineer_names': alignment_engineer_names,
    }

    return render(request, 'assessment_edit.html', context)


def technology_inventory_view(request):
    technology_inventory = TechnologyInventory.objects.all()

    for technology in technology_inventory:
        Customer_id = technology.customer
        cust = Customer.objects.get(pk=Customer_id)
        technology.customer = cust.name

    context = {
        'technology_inventory': technology_inventory,
    }
    return render(request, 'technology_inventory.html', context)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProposedProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows proposed projects to be viewed or edited.
    """

    queryset = ProposedProject.objects.all()
    serializer_class = ProposedProjectSerializer


class AssessmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assessments to be viewed or edited.
    """

    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer


class AssessmentTemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assessment templates to be viewed or edited.
    """

    queryset = AssessmentTemplate.objects.all()
    serializer_class = AssessmentTemplateSerializer


class AssessmentQuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assessment questions to be viewed or edited.
    """

    queryset = AssessmentQuestion.objects.all()
    serializer_class = AssessmentQuestionSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recommendations to be viewed or edited.
    """

    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


class RecommendationProposedProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recommendation proposed projects to be viewed or edited.
    """

    queryset = RecommendationProposedProject.objects.all()
    serializer_class = RecommendationProposedProjectSerializer


class TechnologyInventoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows technology inventory to be viewed or edited.
    """

    queryset = TechnologyInventory.objects.all()
    serializer_class = TechnologyInventorySerializer
