# Generated by Django 4.0.2 on 2022-04-18 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_club_customuser_profile_pic_sport_club_admin_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_alter_pledge_supporter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='is_open',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='goal',
            new_name='goal_amount',
        ),
        migrations.AddField(
            model_name='project',
            name='amount_raised',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='other_ways_to_help',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sport_projects', to='users.sport'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_projects', to='users.club'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_comment', to='projects.project')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]