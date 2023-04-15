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
    education_level = models.CharField(max_length=50)
    institution = models.CharField(max_length=50,null=True)
    program = models.CharField(max_length=50)
    estart_date = models.DateField(null=True)
    eend_date = models.DateField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:  
        db_table = "education" 
        
class Work_Experience(models.Model):
    company_name = models.CharField(max_length=50)
    job_tittle = models.CharField(max_length=50)
    suppervisor_name =models.CharField(max_length=50)
    suppervisor_phone =models.CharField(max_length=50)
    wstart_date = models.DateField()
    wend_date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:  
        db_table = "work_experience" 

class Skills(models.Model):
    skills_name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:  
        db_table = "skills" 

class Specialization(models.Model):
    specialization_name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:  
        db_table = "specialization" 
        
class TalentCategories(models.Model):
    talent_cat_name = models.CharField(unique=True ,max_length=50)
    class Meta:  
        db_table = "talent_categries" 
        
class Employer(models.Model):
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:  
        db_table = "employers" 
        
class Talent(models.Model):
    talent_name = models.CharField(max_length=50)
    talentCategories = models.ForeignKey(TalentCategories,on_delete=models.CASCADE,null=True)
    employer = models.ForeignKey(Employer,on_delete=models.CASCADE,null=True)
    duties_and_respo = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    closing_date = models.DateField(null=True)
    class Meta:  
        db_table = "talent" 
        

        
class Application(models.Model):
    STATUS_CHOICES = (
        ('applied', 'Applied'),
        ('rejected', 'Rejected'),
        ('confirm', 'confirm')
       
    )
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    date_applied = models.DateTimeField(auto_now_add=True)

    class Meta:  
        db_table = "application"

        