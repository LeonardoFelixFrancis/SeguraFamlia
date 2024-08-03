from family.models import FamilyNotifications
from family.serializers import FamilyNotificationsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from django.contrib.auth.models import AnonymousUser

class FamilyNotificationsView(APIView):

    def post(self, request):

        with transaction.atomic():
            
            if request.user == AnonymousUser():
                return Response({'error': 'You are not authenticated'}, status=401)

            serializer = FamilyNotificationsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        
            return Response(serializer.data)
        
    def get(self, request):

        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)
        
        family = request.user.person.family

        if family is None:
            return Response({'error': 'You do not have a family'}, status=404)
        
        notifications = FamilyNotifications.objects.filter(family=family)
        serializer = FamilyNotificationsSerializer(notifications, many=True)

        return Response(serializer.data)
    
    def delete(self, request):
        
        with transaction.atomic():
            notification = FamilyNotifications.objects.get(pk=request.data['id'])
            notification.delete()
        
        return Response({'message': 'Notification deleted successfully'})
    
