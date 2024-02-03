from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class User(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class ServiceProvider(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Booking(models.Model):
     # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, null=True)
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=False)

    booking_date = models.DateTimeField(blank=False)

    booking_time = models.TimeField(null=True)
    

    def clean(self):
        super().clean()
        if not self.service_id:
            raise ValidationError({'service': [""]})

        if self.service.provider != self.service_provider:
            raise ValidationError({'service': ["Service provider doesn't offer this service."]})


    def __str__(self):
        return str(self.service)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    feedback = models.TextField(blank=True)

    def clean(self):
        super().clean()
        if not self.service_id:
            raise ValidationError({'service': [""]})

        if self.service.provider != self.service_provider:
            raise ValidationError({'service': ["Service provider doesn't offer this service."]})

        if self.user == self.service.provider.user:
            raise ValidationError({'service_provider': ["You cannot review your own service."]})

    def __str__(self):
        return str(self.rating)
