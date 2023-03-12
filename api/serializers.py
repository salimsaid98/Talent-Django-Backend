from requests import request
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Personal_Skills, Persosonal_Info,Education,Work_Experience,Skills,Personal_img
from django.contrib.auth.models import User
        
class Personal_InfoSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    # def create(self, validated_data):
    #      validated_data['password'] = make_password(validated_data['password'])
    #      return super().create(validated_data)
    
    class  Meta:
         model = Persosonal_Info
         fields = ('id','first_name','second_name','last_name','address','phone','dob','gender','user')
        #  extra_kwargs = {
        #         'image': {'required': False},
        #     }

    # image = serializers.ImageField()
         
class Educationserializer(serializers.ModelSerializer):
    class  Meta:
        model = Education
        fields = ('id','course_name','education_level','estart_date','eend_date','user')
 
class Work_Experienceserializer(serializers.ModelSerializer):
    class  Meta:
        model = Work_Experience
        fields = ('id','company_name','position','wstart_date','wend_date','user')
        
class Skillsserializer(serializers.ModelSerializer):
    class  Meta:
        model = Skills
        fields = ('id','skills_name')            
        
class Personal_imgserializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_img
        fields = ('id','image','bio','user')
    image = serializers.ImageField()
    # url= serializers.PrimaryKeyRelatedField(queryset=Persosonal_Info.objects.all())
    
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

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
#     url = serializers.HyperlinkedIdentityField(
#     view_name='user-detail',
#     lookup_field='id',
#     read_only=True,
#     context={'request': request}  # Add this line
# )
    class Meta:
        model=User
        fields = ('id','username')
        
class Personal_Skillsserializer(serializers.ModelSerializer):
    class  Meta:
        model = Personal_Skills
        fields = ('id','user','skill')   
        
# class UserSkillSerializer(serializers.ModelSerializer):
#     skills_name = serializers.CharField()

#     class Meta:
#         model = User
#         fields = ('id', 'skills_name')