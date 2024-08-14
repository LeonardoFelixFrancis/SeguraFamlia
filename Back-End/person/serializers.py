from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField, DateField,SlugRelatedField, PrimaryKeyRelatedField
from person.models import Person, Kinship
from drf_extra_fields.fields import Base64ImageField
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
    birthdate = DateField(input_formats=['%m/%d/%Y'])

    class Meta:
        model = Person
        fields = ['name', 'age', 'birthdate', 'profile_picture', 'status', 'family', 'family_id','current_coordinates']


class PersonInputSerializer(ModelSerializer):

    profile_picture = Base64ImageField(required=False, allow_null=True)
    birthdate = DateField(input_formats=['%m/%d/%Y', '%Y/%m/%d'])

    class Meta:
        model = Person
        fields = ['name', 'age', 'birthdate', 'profile_picture', 'status', 'current_coordinates']

    def validate(self, attrs):

        if attrs['profile_picture'] is None:
            attrs.pop('profile_picture')
            
        
        return super().validate(attrs)

class CoordinateDefineSerializer(Serializer):

    coordinates = CharField()
