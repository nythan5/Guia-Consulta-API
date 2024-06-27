from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MODALITIES_LIST = [
    ('HR', 'Home Repair'),
    ('RI', 'Reparo Interno'),
    ('TI', 'Trade-In')
]


class Modalitie(models.Model):
    name = models.CharField(choices=MODALITIES_LIST,
                            null=False, max_length=100)
    description = models.CharField(max_length=255)
    user_create = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
