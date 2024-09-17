from django.db import models


# Create your models here

class User(models.Model):
    Name = models.CharField(max_length=30)
    contactno = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.Name
    
class category(models.Model):
    cat_name=models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name
    
class sub_category(models.Model):
    Category_Id=models.ForeignKey(category,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class package(models.Model):
    name=models.CharField(max_length=30)   
    subcat_id=models.ForeignKey(sub_category,on_delete=models.CASCADE)
    details=models.CharField(max_length=40)
    amount=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    

class BOOKING(models.Model):
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Category=models.CharField(max_length=30)
    subcat=models.CharField(max_length=30)
    Package=models.CharField(max_length=30)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Phone_no = models.BigIntegerField()
    Time=models.CharField(max_length=20)
    Email = models.EmailField()
    date=models.DateField()
    Location = models.CharField(max_length=100)
    details=models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return self.First_Name


class Card(models.Model):
    User_Id=models.ForeignKey(User,on_delete=models.CASCADE)
    # Booking_Id=models.ForeignKey(booking,on_delete=models.CASCADE)
    Name=models.CharField(max_length=30)
    card_num=models.BigIntegerField()
    Cvv= models.IntegerField()
    Expiry_Date=models.CharField(max_length=10)
    timestamp=models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.Name

class contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Subject = models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return self.Name
   

    