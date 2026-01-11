from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.filter().delete()
        Leaderboard.objects.filter().delete()
        User.objects.filter().delete()
        Workout.objects.filter().delete()
        Team.objects.filter().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users

        users = []
        users.append(User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True))
        users.append(User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True))
        users.append(User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True))
        users.append(User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True))

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, date=date.today())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, date=date.today())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration=40, date=date.today())

        # Create Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for superheroes', suggested_for='Marvel')
        Workout.objects.create(name='Agility Training', description='Agility workout for superheroes', suggested_for='DC')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
