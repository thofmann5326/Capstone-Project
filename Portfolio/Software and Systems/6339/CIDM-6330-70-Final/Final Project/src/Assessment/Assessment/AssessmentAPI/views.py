from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from .models import Customer, User, Project, ProposedProject, Assessment, AssessmentTemplate, AssessmentQuestion, Recommendation, RecommendationProposedProject, TechnologyInventory
from .serializers import CustomerSerializer, UserSerializer, ProjectSerializer, ProposedProjectSerializer, AssessmentSerializer, AssessmentTemplateSerializer, AssessmentQuestionSerializer, RecommendationSerializer, RecommendationProposedProjectSerializer, TechnologyInventorySerializer


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
