from django.db import models

# Create the model for the user profile with login name, password, email, image, bio, date created, and date updated fields
class Profile(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    bio = models.TextField()
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')

    def __str__(self):
        return self.name
