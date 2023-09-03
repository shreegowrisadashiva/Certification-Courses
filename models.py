from django.db import models

# Create your models here.

class department(models.Model):
    Dept_Name = models.CharField(max_length=30)
    Start_Date = models.CharField(max_length=40)

class Student(models.Model):
    Name = models.CharField(max_length=30)
    Phone_Number = models.CharField(max_length=50)
    Date_of_birth = models.CharField(max_length=60)
    City = models.CharField(max_length=30)
    Town = models.CharField(max_length=50)
    Street_Number = models.CharField(max_length=30)
    House_number = models.CharField(max_length=30)
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    
    website = models.URLField()
     
class Faculty(models.Model):
    Name  = models.CharField(max_length=100)
    Gender  = models.CharField(max_length=30)
    Faculty  = models.CharField(max_length=100)
    Salary = models.CharField(max_length=50)
    Date_of_birth  = models.CharField(max_length=100)
    Grade   = models.CharField(max_length=30)
    Designation = models.CharField(max_length=50)
   # Course  = models.ForeignKey(Course, on_delete=models.CASCADE )
  #  Project = models.ForeignKey(Project, on_delete=models.CASCADE )


class Project(models.Model):
    Duration = models.CharField(max_length=50)
    Area = models.CharField(max_length=100)
    Name = models.CharField(max_length=30)
    assigns = models.ManyToManyField(Faculty)
    works_on= models.ManyToManyField(Student)

class Course(models.Model):
    Name = models.CharField(max_length=100)
    Code = models.CharField(max_length=50)
    teaches = models.ManyToManyField(Faculty)
    studies=models.ManyToManyField(Student)
      
class Payment(models.Model):
    Price = models.CharField(max_length=100)
    Payment_Date = models.CharField(max_length=100)
    Mode_of_Course= models.CharField(max_length=50)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE )

class Customer(models.Model):
     username=models.CharField(max_length=100)
     pwd=models.CharField(max_length=100)
     email=models.EmailField()
     gender=models.CharField(max_length=10)
     Phone=models.BigIntegerField()
     def __str__(self):
         return self.username

class  course(models.Model):
    course_name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    orders=models.ManyToManyField(Customer)
    def __str__(self):
        return self.course_name
