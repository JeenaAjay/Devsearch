from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Profile

#SIGNAL to create profile automatically when a user is created
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            name = user.first_name,
            email = user.email,
            username = user.username,
        )

post_save.connect(createProfile, sender=User)

#SIGNAL to delete a user when corresponding profile is deleted
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_delete.connect(deleteUser, sender=Profile)

#SIGNAL to update Uses when Profile is updated.
def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

post_save.connect(updateProfile, sender=Profile)       