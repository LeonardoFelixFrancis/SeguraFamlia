from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from person.serializers import PersonSerializer, RegisterSerializer
from django.contrib.auth.models import User, AnonymousUser
from person.models import Person

from django.db import transaction

# Create your views here.
class PersonView(APIView):

    def post(self, request):
        
        with transaction.atomic():
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

        return Response(PersonSerializer(new_Person).data)
    
    def get(self, request):
        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)
        return Response(PersonSerializer(request.user.person).data)
    
    def put(self, request):

        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)

        serializer = PersonSerializer(request.user.person, data=request.data, partial=True)
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
        
        return Response(PersonSerializer(person).data)

class PeopleListView(APIView):

    def get(self, request):
        if request.user == AnonymousUser():
            return Response({'error': 'You are not authenticated'}, status=401)
        
        people = Person.objects.all()
        return Response(PersonSerializer(people, many=True).data)        
