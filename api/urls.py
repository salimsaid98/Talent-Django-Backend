from django.urls import path ,include
from .import views 
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterAPI,LoginAPI, UserSkillsView,UserDetailView
from knox import views as knox_views
router = routers.DefaultRouter()
router.register('personal_info',views.Personal_InfoView)
router.register('education',views.EducationView)
router.register('work_eperience',views.Work_ExperienceView)
router.register('skills',views.SkillsView)
router.register('personal_skills',views.Personal_SkillsView)
router.register('Personal_image',views.Personal_imgView)


# router.register('login',views.LoginSerializer)

# router.register('search_skills',views.LiveSearchView)

 
urlpatterns = [
    path('', include(router.urls)),
    path('search/', views.LiveSearchView.as_view(), name='live-search'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user-information/<id>/', UserDetailView.as_view(), name='user-information'),
    path('userskills/', UserSkillsView.as_view(), name='userskills'),
    #  path('login/?=<user_name>,<email>,<password>', views.LoginView.as_view(), name='login'),
     
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)