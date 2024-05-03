from django.urls import include, path
from rest_framework import routers

from . import views

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

app_name = "AssessmentAPI"

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]

urlpatterns += router.urls
