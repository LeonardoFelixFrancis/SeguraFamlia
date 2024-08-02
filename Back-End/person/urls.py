from django.urls import path
from person.views import PersonView, PeopleListView, OtherPeopleView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [ 
    path('person/', PersonView.as_view(), name='person'),
    path('other_people/', OtherPeopleView.as_view(), name='other_people'),
    path('people_list/', PeopleListView.as_view(), name='people_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]