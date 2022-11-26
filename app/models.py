from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Rather Not Say", "Rather Not Say"),
)
#
# TIME_CHOICES = (
#     ("Morning", "11 AM"),
#     ("Noon", "12 PM"),
#     ("Afternoon", "2 PM"),
#     ("Evening", "4 PM"),
#     ("Night", "8 PM")
# )

DESCRIPTION = (
    ("Pure with no casein", "Fresh Milk"),
    ("Vanilla", "Yoghurt"),
    ("Strawberry", "Yoghurt"),
    ("Milky", "Cheese"),
    ("Creamy", "Ice Cream")
)

# Create your models here.


class Customer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer


class Product(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, choices=DESCRIPTION, default="Cheese")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Rather Not Say")
    # time_of_day = models.CharField(max_length=20, choices=TIME_CHOICES, default="Noon")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer
