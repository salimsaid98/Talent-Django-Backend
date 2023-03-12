from django.db.models import Q,F
from django.contrib.auth import authenticate
from rest_framework import generics, status
from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework import viewsets,generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login

from .models import User,Education,Persosonal_Info,Skills,Work_Experience,Personal_img
from .serializers import Educationserializer, Personal_Skillsserializer,RegisterSerializer,Personal_InfoSerializer, UserSerializer,Work_Experienceserializer,Skillsserializer,Personal_imgserializer
from django.db import connection, models
# # Create your views here.
# class UserView(viewsets.ModelViewSet):
#      queryset = User.objects.all()
#      serializer_class = Userserializer

class Personal_InfoView(viewsets.ModelViewSet):
     queryset = Persosonal_Info.objects.all()
     serializer_class = Personal_InfoSerializer
     
class EducationView(viewsets.ModelViewSet):
     queryset = Education.objects.all()
     serializer_class = Educationserializer
     
class Work_ExperienceView(viewsets.ModelViewSet):
     queryset = Work_Experience.objects.all()
     serializer_class = Work_Experienceserializer
     
class SkillsView(viewsets.ModelViewSet):
     queryset = Skills.objects.all()
     serializer_class = Skillsserializer
     # filter_backends = [DjangoFilterBackend]
     # filterset_fields = ['skills_name', 'skills_category']
   
class LiveSearchView(generics.ListAPIView):
    serializer_class = Skillsserializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query is not None:
            return Skills.objects.filter(
                Q(skills_name__icontains=query) |
                Q(skills_category__icontains=query) 
                
            )
        return Skills.objects.none()

class Personal_imgView(viewsets.ModelViewSet):
     queryset = Personal_img.objects.all()
     serializer_class = Personal_imgserializer
     

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
 
 # Login API       
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = AuthToken.objects.create(user)[1]
        return Response({
            'user': user.id,
            'token': token,
        })
        
        
# get personal infos by passing foreign key
# class UserInformationView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_user_data(self, request,user):
        personal_info = Persosonal_Info.objects.get(user=user)
        education = Education.objects.filter(user=user)
        work_experience = Work_Experience.objects.filter(user=user)
        # skills = Skills.objects.filter(user=user)

        data = {
        'personal_info': Personal_InfoSerializer(personal_info, context={'request': request}).data,
        'education': Educationserializer(education, many=True, context={'request': request}).data,
        'work_experience': Work_Experienceserializer(work_experience, many=True, context={'request': request}).data,
        # 'skills': Skillsserializer(skills, many=True, context={'request': request}).data
    }

        return Response(data)
    
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return self.get_user_data(request, user)
    
class Personal_SkillsView(viewsets.ModelViewSet):
     queryset = Skills.objects.all()
     serializer_class = Personal_Skillsserializer
     
class UserSkillsView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT auth_user.id, auth_user.username, persosonal_info.first_name, persosonal_info.second_name, persosonal_info.last_name, persosonal_info.address, persosonal_info.phone, persosonal_info.dob, persosonal_info.gender, education.course_name, education.education_level, education.estart_date, education.eend_date, work_experience.company_name, work_experience.position, work_experience.wstart_date, work_experience.wend_date, GROUP_CONCAT(DISTINCT skills.skills_name SEPARATOR ', ') AS skills_list, work_experience.company_name FROM auth_user LEFT JOIN persosonal_info ON auth_user.id = persosonal_info.user_id LEFT JOIN education ON auth_user.id = education.user_id LEFT JOIN personal_skills ON auth_user.id = personal_skills.user_id LEFT JOIN skills ON personal_skills.skill_id = skills.id LEFT JOIN work_experience ON auth_user.id = work_experience.user_id GROUP BY auth_user.id HAVING COUNT(DISTINCT skills.skills_name) > 0;")
            rows = cursor.fetchall()
            result = [
                {
                    'id': row[0],
                    'username': row[1],
                    'first_name': row[2],
                    'second_name': row[3],
                    'last_name': row[4],
                    'address': row[5],
                    'phone': row[6],
                    'dob': row[7],
                    'gender': row[8],
                    'course_name': row[9],
                    'education_level': row[10],
                    'estart_date': row[11],
                    'eend_date': row[12],
                    'company_name': row[13],
                    'position': row[14],
                    'wstart_date': row[15],
                    'wend_date': row[16],
                    'skills_list': row[17],
                } for row in rows
            ]
        return Response(result)

from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response

class UserDetailView(APIView):
    def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT auth_user.id, auth_user.username, persosonal_info.first_name, persosonal_info.second_name, persosonal_info.last_name, persosonal_info.address, persosonal_info.phone, persosonal_info.dob, persosonal_info.gender, education.course_name, education.education_level, education.estart_date, education.eend_date, work_experience.company_name, work_experience.position, work_experience.wstart_date, work_experience.wend_date, GROUP_CONCAT(DISTINCT skills.skills_name SEPARATOR ', ') AS skills_list FROM auth_user LEFT JOIN persosonal_info ON auth_user.id = persosonal_info.user_id LEFT JOIN education ON auth_user.id = education.user_id LEFT JOIN personal_skills ON auth_user.id = personal_skills.user_id LEFT JOIN skills ON personal_skills.skill_id = skills.id LEFT JOIN work_experience ON auth_user.id = work_experience.user_id WHERE auth_user.id = %s", [id])
            row = cursor.fetchone()
            if row is not None:
                result = {
                    'id': row[0],
                    'username': row[1],
                    'first_name': row[2],
                    'second_name': row[3],
                    'last_name': row[4],
                    'address': row[5],
                    'phone': row[6],
                    'dob': row[7],
                    'gender': row[8],
                    'course_name': row[9],
                    'education_level': row[10],
                    'estart_date': row[11],
                    'eend_date': row[12],
                    'company_name': row[13],
                    'position': row[14],
                    'wstart_date': row[15],
                    'wend_date': row[16],
                    'skills_list': row[17],
                }
                return Response(result)
            else:
                return Response({'detail': 'User not found'}, status=404)
