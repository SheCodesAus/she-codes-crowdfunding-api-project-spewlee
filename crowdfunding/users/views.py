from django.http import Http404
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Club, CustomUser, Sport
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, ClubSerializer, ClubDetailSerializer, SportSerializer


# TRY SIMPLIFY THIS IN THE FUTURE BY USING generics.ListAPIView and generics.RetrieveUpdateDestroyAPIView

# Display a list of all users
class CustomUserList(APIView):

    def get(self, request):
          users = CustomUser.objects.all()
          serializer = CustomUserSerializer(users, many=True)
          return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# Give a new user a token
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

# Display a single user and allow them to edit
class CustomUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
          try:
               return CustomUser.objects.get(pk=pk)
          except CustomUser.DoesNotExist:
               raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Display all of the clubs
class ClubList(APIView):
    
    def get(self, request):
          clubs = Club.objects.all()
          serializer = ClubSerializer(clubs, many=True)
          return Response(serializer.data)

# Create a club
    def post(self, request):
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# Display and edit a single club
class ClubDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
          try:
               return Club.objects.get(pk=pk)
          except Club.DoesNotExist:
               raise Http404

    def get(self, request, pk):
        club = self.get_object(pk)
        serializer = ClubDetailSerializer(club)
        return Response(serializer.data)

    def put(self, request, pk):
        club = self.get_object(pk)
        data = request.data
        serializer = ClubDetailSerializer(
            instance=club,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Display all the sports (categories)
class SportList(APIView):
    
    def get(self, request):
          sports = Sport.objects.all()
          serializer = SportSerializer(sports, many=True)
          return Response(serializer.data)

    def post(self, request):
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# Display a single sport (category)
class SportDetail(APIView):

    def get_object(self, pk):
        try:
            return Sport.objects.get(pk=pk)
        except Sport.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        sport = self.get_object(pk)
        serializer =SportSerializer(sport)
        return Response(serializer.data)