from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from djongo import models as djongo_models

from django.apps import apps

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        Team = self.get_or_create_team_model()
        Activity = self.get_or_create_activity_model()
        Leaderboard = self.get_or_create_leaderboard_model()
        Workout = self.get_or_create_workout_model()

        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne')
        ironman.profile.team = marvel
        ironman.profile.save()
        batman.profile.team = dc
        batman.profile.save()

        # Create Activities
        Activity.objects.create(user=ironman, type='Running', duration=30)
        Activity.objects.create(user=batman, type='Cycling', duration=45)

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=batman, score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

    def get_or_create_team_model(self):
        class Team(djongo_models.Model):
            name = djongo_models.CharField(max_length=100, unique=True)
            def __str__(self):
                return self.name
        return Team

    def get_or_create_activity_model(self):
        User = get_user_model()
        class Activity(djongo_models.Model):
            user = djongo_models.ForeignKey(User, on_delete=djongo_models.CASCADE)
            type = djongo_models.CharField(max_length=50)
            duration = djongo_models.IntegerField()
        return Activity

    def get_or_create_leaderboard_model(self):
        User = get_user_model()
        class Leaderboard(djongo_models.Model):
            user = djongo_models.ForeignKey(User, on_delete=djongo_models.CASCADE)
            score = djongo_models.IntegerField()
        return Leaderboard

    def get_or_create_workout_model(self):
        class Workout(djongo_models.Model):
            name = djongo_models.CharField(max_length=100)
            description = djongo_models.TextField()
        return Workout
