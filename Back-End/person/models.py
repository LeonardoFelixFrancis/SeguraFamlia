from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Person(models.Model):

    class Status(models.IntegerChoices):

        AT_HOME = 1, _('At Home')
        AT_WORK = 2, _('At Work')
        AT_SCHOOL = 3, _('At School')
        IN_TRANSFER = 4, _('In Transfer')
        IN_OPEN_PLACE = 5, _('In Open Place')
        IN_BUILDING = 6, _('In Building')

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birthdate = models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    status = models.IntegerField(choices=Status.choices, default=Status.AT_HOME)
    family = models.ForeignKey('family.Family', on_delete=models.CASCADE, related_name='members', blank=True, null=True)
    current_coordinates = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='person', editable=False)

    def __str__(self):
        return f'{self.name} {self.family.surname}' if self.family else self.name

class Kinship(models.Model):

    class KinshipType(models.IntegerChoices):

        PARENT = 1, _('Parent')
        CHILD = 2, _('Child')
        SIBLING = 3, _('Sibling')
        SPOUSE = 4, _('Spouse')
        GRANDPARENT = 5, _('Grandparent')
        GRANDCHILD = 6, _('Grandchild')
        AUNT_UNCLE = 7, _('Aunt/Uncle')
        NEPHEW_NIECE = 8, _('Nephew/Niece')
        COUSIN = 9, _('Cousin')
        IN_LAW = 10, _('In Law')
        FRIEND = 11, _('Friend')

    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='kinships')
    related_person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='related_kinships')
    kinship_type = models.IntegerField(choices=KinshipType.choices)

    def __str__(self):
        return f'{self.person} is a {self.kinship_type} of {self.related_person}'