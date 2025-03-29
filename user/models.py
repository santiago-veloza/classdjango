from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Se usará el email en lugar del username
    REQUIRED_FIELDS = ['username']  # Asegura que el username siga existiendo

    def __str__(self):
        return self.email  # Representación del usuario en el admin
