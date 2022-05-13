from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('authenticate/', views.CustomObtainAuthToken.as_view()),
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('users/clubs/', views.ClubList.as_view()),
    path('users/clubs/<int:pk>/', views.ClubDetail.as_view()),
    path('users/sports/', views.SportList.as_view()),
    path('users/sports/<int:pk>/', views.SportDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)