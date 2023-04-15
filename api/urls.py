from django.urls import path ,include
from .import views 
from django.conf.urls.static import static
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import CV_StatusAPIView, EducationListAPIView,ApplicatntAPIView, Personal_infoListAPIView, RegisterAPI,LoginAPI, SkillListAPIView, TalentByIdAPIView, TalentCatByIdAPIView, TalentCategoryCountView, TalentViewlist, User_Application_Status, User_ApplicationList,Work_ExperienceListAPIView,SpecializationListAPIView
from knox import views as knox_views
router = routers.DefaultRouter()
router.register('personal_info',views.Personal_InfoView)
router.register('education',views.EducationView)
router.register('work_eperience',views.Work_ExperienceView)
router.register('skills',views.SkillsView)
router.register('specializtion',views.SpecializtionView)
router.register('talent_cat',views.Talent_catView)
router.register('talent',views.TalentView)
router.register('employer',views.EmployerView)
router.register('application',views.ApplicationView)
 
urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user_skills/<id>/',SkillListAPIView.as_view(), name='skill-detail'),
    path('user_education/<id>/',EducationListAPIView.as_view(), name='education-detail'),
    path('user_personal_info/<id>/',Personal_infoListAPIView.as_view(), name='personal-detail'),
    path('user_work_experience/<id>/',Work_ExperienceListAPIView.as_view(), name='work-exp-detail'),
    path('user_specialization/<id>/',SpecializationListAPIView.as_view(), name='specialization-detail'),
    path('user_talent-cat/<id>/',TalentCatByIdAPIView.as_view(), name='talent-detail'),
    path('talent-category-count/',TalentCategoryCountView.as_view(), name='talent_category_count'),
    path('user-talent-list/', TalentViewlist.as_view(), name='talent_view'),
    path('user_talent-by-id/<id>/',TalentByIdAPIView.as_view(), name='talent-detail'),
    path('employers-applicant_talent/<id>/',ApplicatntAPIView.as_view(), name='talent-detail'),
    path('user-cv-status/<id>/',CV_StatusAPIView.as_view(), name='cv-status'),
    path('user-application/<id>/',User_ApplicationList.as_view(), name='user-application-list'),
    path('user-application-status/<id>/',User_Application_Status.as_view(), name='user-application-status'),


   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)