from django.db import models

# Create your models here.
class Recieved_data(models.Model):
    tag1=models.IntegerField()
    tag2=models.IntegerField()
    tag3=models.IntegerField()
    tag4=models.IntegerField()
    tag5=models.IntegerField()
    tag6=models.IntegerField()
    tag7=models.IntegerField()
    tag8=models.IntegerField()

class line_graph_data(models.Model):
    tag1=models.IntegerField()
    tag2=models.IntegerField()
    tag3=models.IntegerField()
    tag4=models.IntegerField()
    tag5=models.IntegerField()
    tag6=models.IntegerField()
    tag7=models.IntegerField()
    tag8=models.IntegerField()    

class Cylinder(models.Model):
    tank_name=models.CharField()
    product=models.CharField()
    diameter=models.IntegerField()
    height=models.IntegerField()
    tanks_volume=models.IntegerField()

class Conical(models.Model):
    tank_name=models.CharField()
    product=models.CharField()
    diameter1=models.IntegerField()
    diameter2=models.IntegerField()
    height1=models.IntegerField()
    height2=models.IntegerField()
    tanks_volume=models.IntegerField()    