from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Family(models.Model):

    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.surname} Family'
    
class FamilyNotifications(models.Model):

    class NotificationType(models.IntegerChoices):

        BIRTHDAY = 0, _('Birthday')
        WARNING = 1, _('Warning')
        INFO = 2, _('Information')
        EMERGENCY = 3, _('Emergency')
        OTHER = 4, _('Other')

    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    notification_type = models.IntegerField(choices=NotificationType.choices)
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('person.Person', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.family.surname} Family Notification'
    
class FamilyInvitation(models.Model):

    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='invitations')
    inviter = models.ForeignKey('person.Person', on_delete=models.CASCADE, related_name='invitations_sent')
    invitee = models.ForeignKey('person.Person', on_delete=models.CASCADE, related_name='invitations_received')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.inviter.name} invited {self.invitee.name} to {self.family.surname} Family'
