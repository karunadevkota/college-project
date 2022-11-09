from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = "Contact Table"   


#profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles', null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural="Profile Table"

class Case_Study(models.Model):
    totalcases=models.TextField()
    solvedcases=models.TextField()
    onprogress=models.TextField()
    others=models.TextField()
     
    
    class Meta:
        verbose_name_plural = "Case Study " 
        
# report crime model       
Is_Affected=(('Yes','Yes'),('No','No'),)     
crimetype=(('Robbery','Robbery'),('Domestic Volience','Domestic Volience'),('Sexual Harassment','Sexual Harassment'),('Missing person','Missing person'),)   


class Report(models.Model):   
    crimetype=models.CharField(choices=crimetype, max_length=25)
    victimname=models.TextField(max_length=50)
    email=models.EmailField(max_length=50)
    phonenumber=models.CharField(max_length=25,null=True)
    reportingperson=models.CharField(max_length=50)
    incidentdate=models.DateField(auto_now=False)
    incidentlocation=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    no_of_people=models.TextField(blank=True)
    affected=models.CharField(choices=Is_Affected,max_length=25,null=True) 
    
    def __str__(self):
        return self.victimname
   

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    posted_on = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "News "   
        
class Record(models.Model):
    criminal_name = models.CharField(max_length=100)
    crimetype=models.TextField(blank=True)
    description=models.TextField(max_length=500)
    age=models.IntegerField()
    address=models.TextField(max_length=100)
    
    case_status=models.CharField(max_length=100)
    case_start_date = models.DateTimeField(auto_now=False)
     
    def __str__(self):
        return self.criminal_name
    
    class Meta:
        verbose_name_plural = "Criminal Records "   
        
#chart data
class ChartData(models.Model):
    robbery=models.IntegerField()
    domestic_violence=models.IntegerField()
    sexual_harrasement=models.IntegerField()
    missing=models.IntegerField()
    def __str__(self):
        return(self.robbery),(self.domestic_violence),(self.sexual_harrasement),(self.missing)