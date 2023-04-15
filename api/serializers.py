
from rest_framework import serializers
from .models import  Application, Persosonal_Info,Employer,Education,Work_Experience,Skills,Specialization,TalentCategories,Talent
from django.contrib.auth.models import User
        
class Personal_InfoSerializer(serializers.ModelSerializer):
    class  Meta:
         model = Persosonal_Info
         fields = ('id','first_name','second_name','last_name','address','phone','dob','gender','user')
         image = serializers.ImageField()

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['company_name', 'industry', 'address', 'city', 'state', 'country', 'website', 'email', 'phone_number', 'contact_person','user']

         
class Educationserializer(serializers.ModelSerializer):
    class  Meta:
        model = Education
        fields = ('id','education_level','program','institution','estart_date','eend_date','user')

class Skillsserializer(serializers.ModelSerializer):
    class  Meta:
        model = Skills
        fields = ('id','skills_name','user')

class Specializationserializer(serializers.ModelSerializer):
    class  Meta:
        model = Specialization
        fields = ('id','specialization_name','user')
 
class Work_Experienceserializer(serializers.ModelSerializer):
    class  Meta:
        model = Work_Experience
        fields = ('id','company_name','job_tittle','suppervisor_name','suppervisor_phone','wend_date','wstart_date','user')
               
class Talent_catserializer(serializers.ModelSerializer):
    class  Meta:
        model = TalentCategories
        fields = ('id','talent_cat_name')    

class Talentserializer(serializers.ModelSerializer):
    class  Meta:
        model = Talent
        fields = ('id','talent_name','talentCategories','employer','closing_date','duties_and_respo','qualification') 

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'   

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id','username') 
        
