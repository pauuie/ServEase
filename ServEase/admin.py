from django.contrib import admin
from .models import User, ServiceProvider, Service, Booking, Review

admin.site.register(User)
admin.site.register(ServiceProvider)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(Review)
