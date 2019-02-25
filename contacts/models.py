"""
Contacts Models
"""
from django.db import models
from datetime import datetime


class Contact(models.Model):
    """
    Contact from a prospective customer
    """
    contact_date = models.DateField(default=datetime.now, blank=True)
    email = models.CharField(max_length=50)
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField(blank=True, null=True, verbose_name="Listing ID")
    message = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    user_id = models.IntegerField(blank=True, null=True, verbose_name="User ID")

    def __str__(self):
        return f"{self.listing} from {self.name}"
