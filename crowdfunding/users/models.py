from django.contrib.auth.models import AbstractUser
from django.db import models


# User Model
class CustomUser(AbstractUser):
    admin = models.BooleanField(default=False)
    profile_pic = models.URLField(null=True)
    club = models.ForeignKey(
        "users.Club",
        on_delete=models.CASCADE,
        related_name= "user_club",
        null= True
        )

    def __str__(self):
        return self.username



# Club Model
class Club(models.Model):
    name = models.CharField(max_length=200)
    team_colour_1 = models.CharField(max_length=7)
    team_colour_2 = models.CharField(max_length=7)
    facebook_url = models.URLField()
    instagram_url = models.URLField()
    linkedin_url = models.URLField()
    website_url = models.URLField()
    contact_number = models.CharField(max_length=10)
    club_email = models.EmailField()
    description = models.TextField()
    logo = models.URLField()
    slug = models.SlugField()
    sport = models.ForeignKey(
        "users.Sport",
        on_delete=models.CASCADE,
        related_name = "club_sport"
        )
    admin = models.ManyToManyField(
        "users.CustomUser",
        related_name = "club_admin"
        )
    member = models.ManyToManyField(
        "users.CustomUser",
        related_name = "club_member"
        )

    def __str__(self):
        return self.name


    # Sport Category Model
class Sport(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    sport_clubs = models.ManyToManyField(
        "users.Club",
        related_name= "sport_clubs"
    )

    def __str__(self):
        return self.name
