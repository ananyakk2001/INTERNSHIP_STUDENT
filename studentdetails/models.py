from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Batch(models.Model):
       DEPARTMENT =(
           ('MCA','MCA'),
           ('MBA','MBA'),
           ('MA','MA')
       )
       school = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
       year = models.CharField(max_length=100)
       batch_name=models.CharField(max_length=100,choices=DEPARTMENT,null=True,blank=True)
       def __str__(self):
        return self.batch_name

class Student(models.Model):
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

            
            
            

        

        
