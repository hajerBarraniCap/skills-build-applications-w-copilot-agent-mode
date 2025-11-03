from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Modèles simples pour la population (à remplacer par les vrais modèles si existants)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user_email = models.EmailField()
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Nettoyage
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Création des équipes
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Utilisateurs super héros
        users = [
            {'email': 'ironman@marvel.com', 'username': 'Iron Man', 'team': marvel},
            {'email': 'spiderman@marvel.com', 'username': 'Spider-Man', 'team': marvel},
            {'email': 'batman@dc.com', 'username': 'Batman', 'team': dc},
            {'email': 'superman@dc.com', 'username': 'Superman', 'team': dc},
        ]
        for u in users:
            user = User.objects.create_user(email=u['email'], username=u['username'], password='password')
            # Activités
            Activity.objects.create(name='Course', user_email=u['email'], team=u['team'].name)
            # Leaderboard
            Leaderboard.objects.create(user_email=u['email'], team=u['team'].name, points=100)
            # Workouts
            Workout.objects.create(name='Entraînement 1', description='Routine de base', user_email=u['email'])

        self.stdout.write(self.style.SUCCESS('octofit_db a été peuplée avec des données de test.'))
