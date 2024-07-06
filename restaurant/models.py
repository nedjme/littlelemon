from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=200)
    booking_date = models.DateField()
    num_of_guests = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
   title = models.CharField(max_length=200)
   price = models.IntegerField(null=False)
   inventory = models.IntegerField(null=False)

   def __str__(self):
      return self.title
