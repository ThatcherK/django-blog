from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=400)
    picture = models.ImageField(blank=True)
    created_date = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return self.name

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(blank=True)
    bio = models.CharField(blank=True, max_length=200)

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:     
#         Profile.objects.create(user=instance)
        
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save() 
