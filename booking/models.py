from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import uuid

from radcliffeHackBackend import settings

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

class Inventory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pending_appointment = models.IntegerField(blank=True, null=True)
    completed_appointment = models.IntegerField(blank=True, null=True)
    total_appointment = models.IntegerField(blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Test(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=200, blank=True, null=True)
    patient_age = models.IntegerField(blank=True, null=True)
    mobile_number = models.BigIntegerField(blank=True, null=True)
    test_category = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, blank=True, null=True)
    test_type = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    remarks = models.CharField(default='', max_length=300,blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient_name
