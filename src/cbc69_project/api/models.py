from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import datetime


class UserProfileManager(BaseUserManager):
    """Class required by Django for managing our users from the management
    command.
    """

    def create_user(self, email, lastname, firstname, license_number, password=None):
        """Creates a new user with the given detials."""

        # Check that the user provided an email.
        if not email:
            raise ValueError('Users must have an email address.')

        # Create a new user object.
        user = self.model(
            email=self.normalize_email(email),
            lastname=lastname,
            firstname=firstname,
            license_number=license_number,
        )

        # Set the users password. We use this to create a password
        # hash instead of storing it in clear text.
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, lastname, firstname, license_number, password):
        """Creates and saves a new superuser with given detials."""

        # Create a new user with the function we created above.
        user = self.create_user(
            email,
            lastname,
            firstname,
            license_number,
            password
        )

        # Make this user an admin.
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """A user profile in our system."""

    # Django fields
    email = models.EmailField(max_length=255)
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Club fields
    license_number = models.IntegerField(unique=True)
    address = models.CharField(max_length=200, null=True)
    zip_code = models.IntegerField(null=True)
    city = models.CharField(max_length=100, null=True)
    is_coach = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'license_number'
    REQUIRED_FIELDS = ['email', 'lastname', 'firstname']

    def get_full_name(self):
        """
        Required function so Django knows what to use as the users full name.
        """

        return self.firstname + ' ' + self.lastname

    def get_short_name(self):
        """
        Required function so Django knows what to use as the users short name.
        """

        return self.firstname

    def __str__(self):
        """What to show when we output an object as a string."""

        return str(self.license_number) + ' ' + str(self.email)


class StatusUpdate(models.Model):
    """A users status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    """A users message from one user to another."""

    sender = models.ForeignKey('UserProfile', related_name='fk_message_sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        'UserProfile', related_name='fk_message_recipient', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date_sent = models.DateTimeField(auto_now_add=True)


class Tournament(models.Model):
    """A tournament and its details."""

    name = models.CharField(max_length=300)
    description = models.TextField()
    date_beginning = models.DateField()
    date_ending = models.DateField()
    one_day_price = models.IntegerField()
    two_days_price = models.IntegerField()
    trhee_days_price = models.IntegerField()
    authorized_rankings = models.CharField(max_length=100)
    end_of_subscription = models.DateField()
    tournament_type = models.CharField(max_length=100)
    age_category = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=100)
    creator = models.ForeignKey('UserProfile', related_name='fk_tournament_creator', on_delete=models.CASCADE)
    
    objects = models.Manager()

    def __str__(self):
        """What to show when we output the tournament as a string."""

        return 'Tournoi de ' + str(self.city) + ' ' + str(self.tournament_type) 


class Post(models.Model):
    """A post and its details."""

    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()
    author = models.ForeignKey('UserProfile', related_name='fk_post_author', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        """What to show when we output the post as a string."""

        return self.title + ' ' + str(self.date)
    

class Volunteering(models.Model):
    """A volunteering act and its details."""

    title = models.CharField(max_length=300)
    description = models.TextField()
    date_beginning = models.DateTimeField()
    date_ending = models.DateTimeField()
    creator = models.ForeignKey('UserProfile', related_name='fk_volunteering_creator', on_delete=models.CASCADE)
    nb_of_persons_needed = models.IntegerField()
    address = models.CharField(max_length=300)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        """What to show when we output the post as a string."""

        return 'Bénévolat ' + self.title


class InterclubTeam(models.Model):
    """An interclub team and its details."""

    division = models.CharField(max_length=100)
    nb_of_tournament_per_season = models.IntegerField()
    captain = models.ForeignKey('UserProfile', related_name='fk_interclubteam_captain', on_delete=models.CASCADE)
    current_ranking = models.IntegerField()
    nb_of_teams = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        """What to show when we output the interclub team as a string."""

        return 'Equipe Interclub ' + self.division