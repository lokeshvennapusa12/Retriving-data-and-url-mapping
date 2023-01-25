from django.db import models

class Coustomer_details(models.Model):
    Coustomer_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    ph_number=models.IntegerField()
    address=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.IntegerField()
    Coustomer_id=models.ForeignKey(Coustomer_details,on_delete=models.CASCADE)
    order_name=models.CharField(max_length=100)
    order_date=models.DateField(auto_now=True)
    amount=models.IntegerField()
    del_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_name
        


