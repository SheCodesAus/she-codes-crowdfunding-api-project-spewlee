from rest_framework import serializers
from .models import CustomUser, Club, Sport

# TRY SIMPLIFY THIS IN THE FUTURE BY USING serializers.ModelSerializer

# User Serializer
class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    profile_pic = serializers.URLField()
    admin = serializers.BooleanField()
    club = serializers.ReadOnlyField(source='club.id')

    def create(self, validated_data):
          return CustomUser.objects.create(**validated_data)



class CustomUserDetailSerializer(CustomUserSerializer):
    
    def update(self, instance, validated_data):
        instance.profile_pic = validated_data.get('profile_pic', instance.amount)
        instance.admin = validated_data.get('admin', instance.admin)
        instance.club = validated_data.get('club', instance.club)
        instance.save()
        return instance



# Club Serializer
class ClubSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    team_colour_1 = serializers.CharField(max_length=7)
    team_colour_2 = serializers.CharField(max_length=7)
    facebook_url = serializers.URLField()
    instagram_url = serializers.URLField()
    linkedin_url = serializers.URLField()
    website_url = serializers.URLField()
    contact_number = serializers.CharField(max_length=10)
    club_email = serializers.EmailField()
    description = serializers.CharField(max_length=None)
    logo = serializers.URLField()
    slug = serializers.SlugField()
    sport = serializers.ReadOnlyField(source='sport.id')
    admin = serializers.ReadOnlyField(source='admin.id')
    member = serializers.ReadOnlyField(source='member.id')

    def create(self, validated_data):
          return Club.objects.create(**validated_data)



class ClubDetailSerializer(ClubSerializer):

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.team_colour_1 = validated_data.get('team_colour_1', instance.team_colour_1)
        instance.team_colour_2 = validated_data.get('team_colour_2', instance.team_colour_2)
        instance.facebook_url = validated_data.get('facebook_url', instance.facebook_url)
        instance.instagram_url = validated_data.get('instagram_url', instance.instagram_url)
        instance.linkedin_url = validated_data.get('linkedin_url', instance.linkedin_url)
        instance.website_url = validated_data.get('website_url', instance.website_url)
        instance.contact_number = validated_data.get('contact_number', instance.contact_number)
        instance.club_email = validated_data.get('club_email', instance.club_email)
        instance.description = validated_data.get('description', instance.description)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.sport = validated_data.get('sport', instance.sport)
        instance.admin = validated_data.get('admin', instance.admin)
        instance.member = validated_data.get('member', instance.member)
        instance.save()
        return instance



# Sport Category Serializer
class SportSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=100)
    slug = serializers.SlugField()
    sport_projects = serializers.ReadOnlyField(source='sport_projects.id')
    sport_clubs = serializers.ReadOnlyField(source='sport_clubs.id')

    def create(self, validated_data):
          return Sport.objects.create(**validated_data)