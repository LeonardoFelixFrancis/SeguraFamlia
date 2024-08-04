from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField, DateField, PrimaryKeyRelatedField
from person.serializers import PersonOutputSerializer
from family.models import Family, FamilyNotifications, FamilyInvitation
from person.models import Person

class FamilyNotificationsSerializer(ModelSerializer):

    class Meta:
        model = FamilyNotifications
        fields = '__all__'

class FamilySerializer(ModelSerializer):

    members = PersonOutputSerializer(many=True, read_only=True)
    notifications = FamilyNotificationsSerializer(many=True, read_only=True)

    class Meta:
        model = Family
        fields = '__all__'

        read_only_fields = ['members','notifications']


class FamilyInvitationSerializer(ModelSerializer):

    family = PrimaryKeyRelatedField(queryset=Family.objects.all())
    inviter = PrimaryKeyRelatedField(queryset=Person.objects.all())
    invitee = PrimaryKeyRelatedField(queryset=Person.objects.all())

    class Meta:
        model = FamilyInvitation
        fields = '__all__'

class FamilyKickOutSerializer(Serializer):

    member_id = PrimaryKeyRelatedField(queryset=Person.objects.all())
    admin_id = PrimaryKeyRelatedField(queryset=Person.objects.all())
