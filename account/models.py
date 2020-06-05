from django.db import models
from django.conf import settings
from django.contrib.sessions.models import Session


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='profile',on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    session = models.ForeignKey(Session,blank=True, null=True,on_delete=models.CASCADE)    

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
