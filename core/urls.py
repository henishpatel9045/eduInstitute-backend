from django.urls import path
from rest_framework_nested.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("cource", views.CourceViewSet, basename="Cource-ViewSet")

urlpatterns = router.urls
