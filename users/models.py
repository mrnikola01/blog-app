from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Ovde možemo dodati dodatna polja kasnije (npr. bio, profile_picture)
    pass
