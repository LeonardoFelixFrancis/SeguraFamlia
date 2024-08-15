from django.urls import path
from rest_framework.routers import DefaultRouter

from family.views.family_views import (
    FamilyView,
)

from family.views.family_notifications import (
    FamilyNotificationsView
)

family_router = DefaultRouter()
family_router.register('family', FamilyView, basename='family')

urlpatterns = family_router.urls