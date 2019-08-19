from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, default=None)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return str(self.videofile)


