from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    date = models.DateField()
    # pincode = models.CharField(max_length=10)
    def __str__(self):
        return self.name

    




class logIn(models.Model):
    username = models.CharField(max_length= 50)
    fname = models.CharField(max_length= 30)
    lname = models.CharField(max_length= 30)
    email = models.CharField(max_length= 122)
    pass1 = models.CharField(max_length= 50)
    pass2 = models.CharField(max_length= 50)

    def __str__(self):
        return self.username 
    


class logInsignup(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)


