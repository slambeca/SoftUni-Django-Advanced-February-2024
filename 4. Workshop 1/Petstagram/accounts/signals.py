from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from Petstagram.accounts.models import Profile

UserModel = get_user_model()


# Call this function every time when the save method is applied to the UserModel
@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    # created = False when update
    # created = True, when create
    if not created:
        return

    # Eager save (it creates the object and nothing more, the code below is extensible and flexible
    Profile.objects.create(user=instance)
    # same as:
    # profile = Profile(user=instance)
    # profile.save()