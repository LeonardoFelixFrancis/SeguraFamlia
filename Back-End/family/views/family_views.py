from django.shortcuts import render
from rest_framework.views import APIView
from family.models import Family, FamilyInvitation
from rest_framework.response import Response
from family.serializers import FamilySerializer, FamilyInvitationSerializer, FamilyKickOutSerializer
from django.db import transaction
from django.contrib.auth.models import User, AnonymousUser
from family.services.family_service import FamilyService
# Create your views here.

class FamilyView(APIView):

    def post(self, request):

        with transaction.atomic():
            
            if request.user == AnonymousUser():
                return Response({'error': 'You are not authenticated'}, status=401)

            serializer = FamilySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        
            return Response(serializer.data)
    
    def get(self, request):
        
        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)
        
        person = request.user.person

        family = person.family

        if family is None:
            return Response({'error': 'You do not have a family'}, status=404)
        
        serializer = FamilySerializer(family)

        return Response(serializer.data)
    
    def put(self, request):
            
        with transaction.atomic():
            
            if request.user == AnonymousUser():
                return Response({'error': 'You are not authenticated'}, status=401)
            
            family = Family.objects.get(pk=request.data['id'])
            serializer = FamilySerializer(family, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(serializer.data)
    
    def delete(self, request):
        
        with transaction.atomic():
            family = Family.objects.get(pk=request.data['id'])
            family.delete()
        
        return Response({'message': 'Family deleted successfully'})
    
class InviteForFamilyView(APIView):

    family_service = FamilyService()

    def post(self, request):

        with transaction.atomic():
            
            if request.user == AnonymousUser():
                return Response({'error': 'You are not authenticated'}, status=401)

            data = request.data

            data['inviter'] = request.user.person.id

            serializer = FamilyInvitationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            family_invitation = self.family_service.InviteForFamily(inviter=serializer.validated_data['inviter'], 
                                                                    invitee=serializer.validated_data['invitee'], 
                                                                    family=serializer.validated_data['family'])
        
            return Response(serializer.data)
        
class AcceptFamilyInvitationView(APIView):

    def post(self, request):

        with transaction.atomic():
            
            if request.user == AnonymousUser():
                return Response({'error': 'You are not authenticated'}, status=401)

            try:
                family_invitation = FamilyInvitation.objects.get(pk=request.data['id'])
            except FamilyInvitation.DoesNotExist:
                return Response({'error': 'Family invitation not found'}, status=404)

            if family_invitation.invitee != request.user.person:
                return Response({'error': 'You are not the invitee'}, status=400)
            
            if family_invitation.accepted:
                return Response({'error': 'Family invitation already accepted'}, status=400)
            
            family_invitation.invitee.family = family_invitation.family

            family_invitation.invitee.save()

            family_invitation.accepted = True

            family_invitation.save()

            return Response({'message': 'Family invitation accepted successfully'})
        
class FamilyKickOutMemberView(APIView):

    family_service = FamilyService()

    def post(self, request):

        with transaction.atomic():

            if request.user == AnonymousUser():
                return Response({'error': 'You are not authenticated'}, status=401)
            
            data = request.data

            data['admin_id'] = request.user.person.id

            serializer = FamilyKickOutSerializer(data=data)
            serializer.is_valid(raise_exception=True)

            member = self.family_service.KickMemberOut(admin=serializer.validated_data['admin_id'], member=serializer.validated_data['member_id'])
        
            return Response(serializer.data)