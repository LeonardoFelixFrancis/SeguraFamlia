from family.models import Family, FamilyNotifications, FamilyInvitation
from family.serializers import FamilySerializer, FamilyNotificationsSerializer, FamilyInvitationSerializer
from person.models import Person
from rest_framework.exceptions import ValidationError

class FamilyService:

    def InviteForFamily(self, inviter:Person, invitee:Person, family:Family) -> FamilyInvitation:
        
        if inviter.family != family:
            raise ValidationError('You are not a member of this family')
        
        if not inviter.is_family_admin:
            raise ValidationError({'error': 'You are not the invitee'})
        
        if inviter == invitee:
            raise ValidationError({'error': 'You are not the invitee'})
        
        if invitee.family == family:
            raise ValidationError({'error': 'You are not the invitee'})

        family_invitation = FamilyInvitation(family=family, inviter=inviter, invitee=invitee)

        family_invitation.save()

        return family_invitation
    
    def KickMemberOut(self, admin:Person, member:Person):
        
        if not admin.is_family_admin:
            raise ValidationError({'error': 'You are not the admin'})
        
        if admin.family != member.family:
            raise ValidationError({"error': 'Your are not in the same family of the member you're trying to kick out"})
        
        if admin == member:
            raise ValidationError({'error': 'You cannot kick yourself out'})
        
        member.family = None
        member.save()
        
        return member