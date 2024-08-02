from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField, DateField
from person.models import Person, Kinship

class RegisterSerializer(Serializer):

    username = CharField()
    password = CharField()
    name = CharField()
    age = IntegerField()
    birthdate = DateField()


class PersonSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'
