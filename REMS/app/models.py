from django.db import models

# Create your models here.

from django.db import models

class Location(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}"

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Property(models.Model):
    property_name = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    status = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.property_name

class Appointment(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Appointment for {self.property.property_name} on {self.date} at {self.time}"

class Feedback(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    comments = models.TextField()
    rating = models.IntegerField()
    feedback_date = models.DateField()

    def __str__(self):
        return f"Feedback for {self.appointment.property.property_name} by {self.appointment.agent.first_name}"

