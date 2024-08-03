from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from person.serializers import PersonInputSerializer, RegisterSerializer, CoordinateDefineSerializer, PersonOutputSerializer
from django.contrib.auth.models import User, AnonymousUser
from person.models import Person
from family.models import Family

from django.db import transaction

# Create your views here.
class PersonView(APIView):

    def post(self, request):
        
        with transaction.atomic():
            print(request.data)
            serializer = RegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            new_user = User.objects.create_user(username=serializer.validated_data['username'], 
                                    password=serializer.validated_data['password'])
            
            new_Person = Person(name=serializer.validated_data['name'],
                                age=serializer.validated_data['age'],
                                birthdate=serializer.validated_data['birthdate'],
                                family=None)

            new_Person.user = new_user

            new_Person.save()

        return Response(PersonInputSerializer(new_Person).data)
    
    def get(self, request):
        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)
        return Response(PersonOutputSerializer(request.user.person).data)
    
    def put(self, request):

        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)

        serializer = PersonInputSerializer(request.user.person, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request):

        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)
        
        request.user.person.delete()
        request.user.delete()
        return Response({'message': 'User deleted successfully'})

class OtherPeopleView(APIView):

    def get(self, request):
        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)
        
        person_id = request.data.get('person_id')

        if person_id is None:
            return Response({'error': 'person_id is required'}, status=400)
        
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)
        
        return Response(PersonOutputSerializer(person).data)

class PeopleListView(APIView):

    def get(self, request):
        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)
        
        people = Person.objects.all()
        return Response(PersonOutputSerializer(people, many=True).data)        

class DefineCoordinatesView(APIView):

    def post(self, request):

        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)

        serializer = CoordinateDefineSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        coordinates = serializer.validated_data['coordinates']

        person = request.user.person

        person.current_coordinates = coordinates

        person.save()

        return Response(serializer.data)
    
class DefineProfilePicture(APIView):

    def post(self, request):

        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)

        image = request.FILES.get('profile_image')

        person = request.user.person

        person.profile_picture = image
        person.save()

        return Response({'message': 'Profile picture updated successfully'})
        
class ChangeStatusView(APIView):

    def post(self, request):

        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)
        
        status = request.data.get('status')

        if status is None:
            return Response({'error': 'status is required'}, status=400)
        
        if status not in Person.Status.values:
            return Response({'error': 'Invalid status'}, status=400)

        person = request.user.person

        person.status = status
        person.save()

        return Response({'message': 'Status updated successfully'})
    