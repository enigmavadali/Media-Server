from django.urls import path
from . import views
app_name = 'authentication'
urlpatterns = [
	path('professor_signup/', views.prof_signup_view, name='prof_signup'),
    path('student_signup/', views.stud_signup_view, name='stud_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
