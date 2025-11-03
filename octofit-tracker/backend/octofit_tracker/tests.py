from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Team, Activity, Leaderboard, Workout
from django.contrib.auth import get_user_model

User = get_user_model()

class APIRootTest(APITestCase):
    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

class TeamTest(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Test Team'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTest(APITestCase):
    def test_create_activity(self):
        url = reverse('activity-list')
        data = {'name': 'Test Activity', 'user_email': 'test@example.com', 'team': 'Test Team'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTest(APITestCase):
    def test_create_leaderboard(self):
        url = reverse('leaderboard-list')
        data = {'user_email': 'test@example.com', 'team': 'Test Team', 'points': 10}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTest(APITestCase):
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'name': 'Test Workout', 'description': 'desc', 'user_email': 'test@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
