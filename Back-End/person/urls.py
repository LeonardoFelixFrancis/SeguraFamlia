from django.urls import path
from person.views import PersonView, PeopleListView, OtherPeopleView, DefineCoordinatesView, DefineProfilePicture, ChangeStatusView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [ 
    path('person/', PersonView.as_view(), name='person'),
    path('other_people/', OtherPeopleView.as_view(), name='other_people'),
    path('people_list/', PeopleListView.as_view(), name='people_list'),
    path('person/define_coordinates/', DefineCoordinatesView.as_view(), name='define_coordinates'),
    path('person/define_profile_picture/', DefineProfilePicture.as_view(), name='define_profile_picture'),
    path('person/change_status/', ChangeStatusView.as_view(), name='change_status'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]