from django.urls import include, path
from rest_framework import routers
from . import views
from .views import get_os_counts

# Define a router for API endpoints
router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'proposed-projects', views.ProposedProjectViewSet)
router.register(r'assessments', views.AssessmentViewSet)
router.register(r'assessment-templates', views.AssessmentTemplateViewSet)
router.register(r'assessment-questions', views.AssessmentQuestionViewSet)
router.register(r'recommendations', views.RecommendationViewSet)
router.register(r'recommendation-proposed-projects',
                views.RecommendationProposedProjectViewSet)
router.register(r'technology-inventory', views.TechnologyInventoryViewSet)

# Define the app name for URL namespaces
app_name = "AssessmentAPI"

# Define URL patterns
urlpatterns = [
    # Default view for customer summary
    path('', views.customer_summary_view, name='customer_summary'),

    # View for customer summary (duplicate for easy access)
    path('customer-summary/', views.customer_summary_view, name='customer_summary'),

    # View for editing assessment
    path('assessment/<int:assessment_id>/edit/',
         views.assessment_edit_view, name='assessment_edit'),

    # View for displaying technology inventory
    path('technology-inventory/', views.technology_inventory_view,
         name='technology_inventory'),

    # View for getting operating system counts
    path('get-os-counts/<int:customer_id>/',
         get_os_counts, name='get_os_counts'),
]
