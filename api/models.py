from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Create your models here.

class Persosonal_Info(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    second_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=50,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:  
        db_table = "persosonal_info" 

class Education(models.Model):
    course_name = models.CharField(max_length=50)
    education_level = models.CharField(max_length=50,null=True)
    estart_date = models.DateField(null=True)
    eend_date = models.DateField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:  
        db_table = "education" 
        
class Work_Experience(models.Model):
    company_name = models.CharField(max_length=50)
    position= models.CharField(max_length=50)
    wstart_date = models.DateField()
    wend_date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:  
        db_table = "work_experience" 

class Skills(models.Model):
    skills_name = models.CharField(max_length=50,unique=True)
    class Meta:  
        db_table = "skills" 

class Personal_Skills(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    skill = models.ForeignKey(Skills,on_delete=models.CASCADE,null=True)
    class Meta:  
        db_table = "Personal_Skills" 
        
class Personal_img(models.Model):
    bio = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/',null=True, blank=True,validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = "images"
        