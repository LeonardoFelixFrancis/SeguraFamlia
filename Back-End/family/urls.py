from django.urls import path

from family.views.family_views import (
    FamilyView
)

from family.views.family_notifications import (
    FamilyNotificationsView
)


urlpatterns = [

    # Family Urls
    path('family/', FamilyView.as_view(), name='family'),
    
    # Family Notifications Urls
    path('family/notifications/', FamilyNotificationsView.as_view(), name='family_notifications')


]