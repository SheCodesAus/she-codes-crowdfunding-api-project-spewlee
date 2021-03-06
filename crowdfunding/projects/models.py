from django.contrib.auth import get_user_model
from django.db import models

# Project Model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    other_ways_to_help = models.TextField(null=True)
    goal_amount = models.IntegerField()
    amount_raised = models.IntegerField(default=0)
    image = models.URLField()
    active = models.BooleanField()
    date_created = models.DateField(auto_now=True)
    due_date = models.DateField(null=True)
    owner = models.ForeignKey(
        "users.Club",
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    sport = models.ForeignKey(
        "users.Sport",
        on_delete=models.CASCADE,
        related_name='sport_projects',
        null=True
    )

    def __str__(self):
        return self.title


# Pledge Model
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.TextField()
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter'
    )



# Comment Model
class Comment(models.Model):
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name='project_comment'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='commenter'
    )
    date = models.DateField(auto_now=True)
    body = models.TextField(blank=False)

    class Meta:
        ordering = ['date']