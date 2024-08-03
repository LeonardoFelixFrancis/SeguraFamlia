from family.models import Family, FamilyNotifications, FamilyInvitation
from family.serializers import FamilySerializer, FamilyNotificationsSerializer, FamilyInvitationSerializer
from person.models import Person

class FamilyService:

    def InviteForFamily(self, inviter:Person, invitee:Person, family:Family) -> FamilyInvitation:
        
        if inviter.family != family:
            return {'error': 'You are not a member of this family'}
        
        if not inviter.is_family_admin:
            return {'error': 'You are not an admin of this family'}
        
        family_invitation = FamilyInvitation(family=family, inviter=inviter, invitee=invitee)

        family_invitation.save()

        return family_invitation