from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Department(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    def save_department(self):
        self.save()

class Programme(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    def save_department(self):
        self.save()


class Coordinator(models.Model):
    coordinatorsNumber = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    regDate = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete= models.PROTECT)

    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)
    
    def save_coordinator(self):
        self.save()
    
       
class Supervisor(models.Model):
    supervisorsNumber = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete= models.CASCADE)
    coordinator = models.ForeignKey(Coordinator, on_delete= models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=CASCADE)
    registrationDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
 
    def __str__(self):
        return self.firstName
    def save_supervisor(self):
        self.save()

class Student(models.Model):
    serialNumber = models.CharField(max_length=10, null=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete= models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete= models.CASCADE)
    registrationDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.firstName

    def save_students(self):
        self.save()

class  SupervisorCharacteristics(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    superOne = models.IntegerField()
    superTwo = models.IntegerField()
    superThree = models.IntegerField()
    superFour = models.IntegerField()
    marks = models.IntegerField()
   

class  StudentCharacteristics(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    studentOne = models.IntegerField()
    studentTwo = models.IntegerField()
    studentThree = models.IntegerField()
    studentFour = models.IntegerField()
    marks = models.IntegerField()
    

class  CoordinatorRateLearning(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    learningOne = models.IntegerField()
    learningTwo = models.IntegerField()
    marks = models.IntegerField()
    

class CoordinatorRateSupervisor(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    superCoorOne = models.IntegerField()
    marks = models.IntegerField()


class testForm(models.Model):
    supervisor =models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    yourname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    totals = models.IntegerField()

    

