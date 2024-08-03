from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField, DateField,SlugRelatedField, PrimaryKeyRelatedField
from person.models import Person, Kinship
from family.models import Family    

class RegisterSerializer(Serializer):

    username = CharField()
    password = CharField()
    name = CharField()
    age = IntegerField()
    birthdate = DateField()

class PersonOutputSerializer(ModelSerializer):

    family = SlugRelatedField(slug_field='surname', read_only=True)
    family_id = IntegerField()

    class Meta:
        model = Person
        fields = ['name', 'age', 'birthdate', 'profile_picture', 'status', 'family', 'family_id','current_coordinates']

class PersonInputSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = ['name', 'age', 'birthdate', 'profile_picture', 'status', 'current_coordinates']

class CoordinateDefineSerializer(Serializer):

    coordinates = CharField()
