from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, UserProfile, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(user=self.user, team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30)
        self.workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user_profile(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.team.name, 'Test Team')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Running')
        self.assertEqual(self.activity.duration, 30)

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Pushups')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 100)
