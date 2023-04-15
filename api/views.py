from itertools import count
from django.db.models import Q,F
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views import View
from rest_framework import generics, status
from django.forms import ValidationError, model_to_dict
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
from django.db import connection
from rest_framework.response import Response
from .models import Application, User,Employer,Education,Persosonal_Info,Skills,Work_Experience,Specialization,TalentCategories,Talent
from .serializers import ApplicationSerializer, Educationserializer,EmployerSerializer,RegisterSerializer,Personal_InfoSerializer, UserSerializer,Work_Experienceserializer,Skillsserializer,Specializationserializer,Talent_catserializer,Talentserializer
from django.db import connection
from rest_framework.generics import RetrieveAPIView

class Personal_InfoView(viewsets.ModelViewSet):
     queryset = Persosonal_Info.objects.all()
     serializer_class = Personal_InfoSerializer

class EmployerView(viewsets.ModelViewSet):
     queryset = Employer.objects.all()
     serializer_class = EmployerSerializer
     
class EducationView(viewsets.ModelViewSet):
     queryset = Education.objects.all()
     serializer_class = Educationserializer
     
class Work_ExperienceView(viewsets.ModelViewSet):
     queryset = Work_Experience.objects.all()
     serializer_class = Work_Experienceserializer
     
class SkillsView(viewsets.ModelViewSet):
     queryset = Skills.objects.all()
     serializer_class = Skillsserializer
     
class SpecializtionView(viewsets.ModelViewSet):
     queryset = Specialization.objects.all()
     serializer_class = Specializationserializer 
     
class Talent_catView(viewsets.ModelViewSet):
     queryset = TalentCategories.objects.all()
     serializer_class = Talent_catserializer   
     
class TalentView(viewsets.ModelViewSet):
     queryset = Talent.objects.all()
     serializer_class = Talentserializer
     
class ApplicationView(viewsets.ModelViewSet):
     queryset = Application.objects.all()
     serializer_class = ApplicationSerializer

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
        
     
# Api for retrieve skills based on there foreign key 
class SkillListAPIView(APIView):
      def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, skills_name  FROM `skills` WHERE user_id = %s", [id])
            rows = cursor.fetchall()
            if len(rows) > 0:
                results = []
                for row in rows:
                    result = {
                        'id': row[0],
                        'skills_name': row[1],
                    }
                    results.append(result)
                return Response(results)
            else:
                return Response({'detail': 'Skill not found'}, status=404)
            
# Api for retrieve specialization based on there foreign key 
class SpecializationListAPIView(APIView):
      def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, specialization_name  FROM `specialization` WHERE user_id = %s", [id])
            rows = cursor.fetchall()
            if len(rows) > 0:
                results = []
                for row in rows:
                    result = {
                        'id': row[0],
                        'specialization_name': row[1],
                    }
                    results.append(result)
                return Response(results)
            else:
                return Response({'detail': 'Skill not found'}, status=404)
            
# Api for retrieve Eduvcation based on there foreign key 
class EducationListAPIView(APIView):
      def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id,education_level, institution ,program, estart_date, eend_date FROM education WHERE user_id  = %s", [id])
            rows = cursor.fetchall()
            if len(rows) > 0:
                results = []
                for row in rows:
                    result = {
                        'id': row[0],
                        'education_level': row[1],
                        'institution': row[2],
                        'program': row[3],
                        'estart_date': row[4],
                        'eend_date': row[5],
                    }
                    results.append(result)
                return Response(results)
            else:
                return Response({'detail': 'Education not found'}, status=404)
# 
class Work_ExperienceListAPIView(APIView):
      def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id,company_name ,job_tittle, suppervisor_name, suppervisor_phone,wstart_date,wend_date FROM work_experience WHERE user_id = %s", [id])
            rows = cursor.fetchall()
            if len(rows) > 0:
                results = []
                for row in rows:
                    result = {
                        'id': row[0],
                        'company_name': row[1],
                        'job_tittle' : row[2],
                        'suppervisor_name' : row[3],
                        'suppervisor_phone' : row[4],
                        'wstart_date': row[5],
                        'wend_date': row[6],
                    }
                    results.append(result)
                return Response(results)
            else:
                return Response({'detail': 'Work_Experience not found'}, status=404)
 # 
class Personal_infoListAPIView(APIView):
      def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id,first_name,second_name,last_name,gender,address,dob,phone FROM persosonal_info WHERE user_id = %s", [id])
            rows = cursor.fetchall()
            if len(rows) > 0:
                results = []
                for row in rows:
                    result = {
                        'id': row[0],
                        'first_name': row[1],
                        'second_name': row[2],
                        'last_name': row[3],
                        'gender': row[4],
                        'address': row[5],
                        'dob': row[6],
                        'phone': row[7],
                    }
                    results.append(result)
                return Response(results)
            else:
                return Response({'detail': 'Personal_info not found'}, status=404)

# Talent Categires By id With Employers 
class TalentCatByIdAPIView(APIView):
      def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT t.id,t.talent_name, t.closing_date, t.duties_and_respo, t.qualification, e.company_name FROM talent t INNER JOIN employers e ON e.id = t.employer_id WHERE t.talentCategories_id = %s", [id])
            rows = cursor.fetchall()
            if len(rows) > 0:
                results = []
                for row in rows:
                    result = {
                        'id': row[0],
                        'talent_name': row[1],
                        'closig_date': row[2],
                        'duties_and_respo': row[3],
                        'qualification': row[4],
                        'company_name': row[5],
                    }
                    results.append(result)
                return Response(results)
            else:
                return Response({'detail': 'Talent not found'}, status=404)
            
# Talent categories Count
class TalentCategoryCountView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT tc.id, tc.talent_cat_name, COUNT(t.id) as talent_count
                FROM talent_categries tc
                LEFT JOIN talent t ON tc.id = t.talentCategories_id
                GROUP BY tc.talent_cat_name;
            """)
            results = cursor.fetchall()

        response_data = []
        for row in results:
            response_data.append({
                'talent_category_id': row[0],
                'talent_category_name': row[1],
                'talent_count': row[2],
            })

        return Response(response_data)
    

class TalentByIdAPIView(APIView):
      def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT t.id,t.talent_name, t.closing_date, t.duties_and_respo, t.qualification, e.company_name,e.id as employer FROM talent t INNER JOIN employers e ON e.id = t.employer_id WHERE t.id = %s", [id])
            rows = cursor.fetchall()
            if len(rows) > 0:
                results = []
                for row in rows:
                    result = {
                        'id': row[0],
                        'talent_name': row[1],
                        'closig_date': row[2],
                        'duties_and_respo': row[3],
                        'qualification': row[4],
                        'company_name': row[5],
                        'employer':row[6]
                    }
                    results.append(result)
                return Response(results)
            else:
                return Response({'detail': 'Talent not found'}, status=404)
    
    
class TalentViewlist(APIView):
     def get(self, request):
        with connection.cursor() as cursor:
                cursor.execute('SELECT t.id, t.talent_name, t.closing_date, t.duties_and_respo, t.qualification, e.company_name FROM talent t INNER JOIN employers e ON e.id = t.employer_id')
                rows = cursor.fetchall()
                if len(rows) > 0:
                        results = []
                        for row in rows:
                            result = {
                                'id': row[0],
                                'talent_name': row[1],
                                'closig_date': row[2],
                                'duties_and_respo': row[3],
                                'qualification': row[4],
                                'company_name': row[5],
                                
                            }
                            results.append(result)
                        return Response(results)
                else:
                  return Response({'detail': 'Talent categories not found'}, status=404)

class ApplicatntAPIView(APIView):
      def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT u.id,u.username,t.talent_name,a.date_applied, a.status FROM auth_user u INNER JOIN application a ON u.id = a.user_id INNER JOIN talent t ON a.talent_id = t.id WHERE a.employer_id = %s", [id])
            rows = cursor.fetchall()
            if len(rows) > 0:
                results = []
                for row in rows:
                    result = {
                        'id': row[0],
                        'username': row[1],
                        'talent_name': row[2],
                        'date_applied': row[3],
                        'status': row[4],
                    }
                    results.append(result)
                return Response(results)
            else:
                return Response({'detail': 'application not found'}, status=404)
            
class CV_StatusAPIView(APIView):
    def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    CASE 
                        WHEN EXISTS (SELECT 1 FROM persosonal_info WHERE user_id = %s) AND
                             EXISTS (SELECT 1 FROM education WHERE user_id = %s) AND
                             EXISTS (SELECT 1 FROM work_experience WHERE user_id = %s) AND
                             EXISTS (SELECT 1 FROM skills WHERE user_id = %s) AND
                             EXISTS (SELECT 1 FROM specialization WHERE user_id = %s)
                        THEN 'Complete'
                        ELSE 'Incomplete'
                    END AS cv_status
                """, [id, id, id, id, id])
            rows = cursor.fetchall()
            if len(rows) > 0:
                result = {'cv_status': rows[0][0]}
                return Response(result)
            else:
                return Response({'detail': 'cv not found'}, status=404)
# user application list
class User_ApplicationList(APIView):
    def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, status, date_applied, talent_id, user_id, employer_id FROM application WHERE user_id = %s", [id])
            results = cursor.fetchall()
            data = [{'id': row[0], 'status': row[1], 'date_applied': row[2], 'talent_id': row[3], 'user_id': row[4], 'employer_id': row[5]} for row in results]
        return Response(data)
    
class User_Application_Status(APIView):
        def get(self,request, id):
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT application.id, application.status, application.date_applied, application.talent_id, 
                    application.user_id, application.employer_id, talent.talent_name 
                    FROM application application 
                    INNER JOIN talent talent on talent.id = application.talent_id 
                    WHERE application.user_id = %s""", [id])
                applications = cursor.fetchall()
                data = [{'id': app[0],
                            'status': app[1],
                            'date_applied': app[2],
                            'talent_id': app[3], 
                            'user_id': app[4], 
                            'employer_id': app[5],
                            'talent_name': app[6]} 
                            for app in applications]
                return Response(data)
