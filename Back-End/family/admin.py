from django.contrib import admin
from family.models import Family, FamilyInvitation, FamilyNotifications

# Register your models here.
admin.site.register(Family)
admin.site.register(FamilyInvitation)
admin.site.register(FamilyNotifications)