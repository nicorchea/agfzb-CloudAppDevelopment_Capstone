from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # add any other fields you would like to include

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=50)
    TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('wagon', 'WAGON'),
        # add any other choices you would like
    ]
    car_type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    year = models.DateField()
    # add any other fields you would like to include

    def __str__(self):
        return f"{self.make.name} {self.name}"


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip, state):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip
        # Dealer state
        self.state = state


    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, id):
        # Dealer dealership
        self.dealership = dealership
        # Dealer name
        self.name = name
        # Dealer purchase
        self.purchase = purchase
        # Dealer review
        self.review = review
        # Location purchase_date
        self.purchase_date = purchase_date
        # Location car_make
        self.car_make = car_make
        # Dealer car_model
        self.car_model = car_model
        # Dealer car_year
        self.car_year = car_year
        # Dealer id
        self.id = id
        # self.another = another

    def __str__(self):
        return "Dealer name: " + self.name
