from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_image = models.ImageField(upload_to='car_images/', blank=True, null=True)


    def __str__(self):
        return f"{self.name} {self.model} - ${self.price}  {self.car_image}"