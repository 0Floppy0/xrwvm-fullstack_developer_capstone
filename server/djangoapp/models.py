from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# ---------------------------
# Car Make Model
# ---------------------------
class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    # Optional field: country of origin
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name}"


# ---------------------------
# Car Model Model
# ---------------------------
class CarModel(models.Model):

    # Relationship: One CarMake -> Many CarModel
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    # Dealer ID (from Cloudant) — now optional to avoid populate errors
    dealer_id = models.IntegerField(null=True, blank=True, default=None)

    name = models.CharField(max_length=50)

    # Type field with limited choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCH', 'Hatchback'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SEDAN')

    # Year: with validators 2015–2023
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    # Optional field: color
    color = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
