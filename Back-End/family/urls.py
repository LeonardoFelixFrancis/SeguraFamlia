from django.urls import path

from family.views.family_views import (
    FamilyView,
    InviteForFamilyView, AcceptFamilyInvitationView, FamilyKickOutMemberView
)

from family.views.family_notifications import (
    FamilyNotificationsView
)


urlpatterns = [

    # Family Urls
    path('family/', FamilyView.as_view(), name='family'),
    path('family/invite/', InviteForFamilyView.as_view(), name='invite_for_family'),
    path('family/invite/accept/', AcceptFamilyInvitationView.as_view(), name='accept_family_invitation'),
    path('family/kickout/', FamilyKickOutMemberView.as_view(), name='kickout_family_member'),

    # Family Notifications Urls
    path('family/notifications/', FamilyNotificationsView.as_view(), name='family_notifications')


]