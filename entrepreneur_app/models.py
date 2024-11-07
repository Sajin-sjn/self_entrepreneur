from django.db import models

# Create your models here.

class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)

class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=100)

class product(models.Model):
    product_id=models.AutoField(primary_key=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    stock=models.CharField(max_length=100)

class booking_master(models.Model):
    booking_master_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    total_amount=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class booking_child(models.Model):
    booking_child_id=models.AutoField(primary_key=True)
    booking_master=models.ForeignKey(booking_master,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)

class rating(models.Model):
    rating_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    rating=models.CharField(max_length=100)
    date=models.CharField(max_length=100)

class payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    booking_master=models.ForeignKey(booking_master,on_delete=models.CASCADE)
    amount=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    


