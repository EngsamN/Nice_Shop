# account/models.py

from django.db import models

class UserProfile(models.Model):
    """
    Represents a user profile in the system.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model.
        bio (TextField): The user's biography.
        birth_date (DateField): The user's birth date.
    """

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the user profile.

        Returns:
            str: A string containing the user's username.
        """
        return self.user.username
