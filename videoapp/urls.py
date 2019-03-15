from django.urls import path
from . import views
# sandy 123

app_name = "videoapp"
urlpatterns = [
	path('', views.home, name="home"),
	#path('upload', views.upload, name="upload"),
	path('admin_upload', views.admin_upload, name="admin_upload"),
    path('professor_upload', views.professor_upload, name="prof_upload"),
    path('lecture/<int:ID>', views.play_lecture, name='play_prof'),
	path('like/<int:ID>', views.like, name='like'),
	path('comment/<str:obj_type>/<int:ID>', views.comment, name='comment'),
	path('reg_student_for_video/<int:ID>', views.reg_student_for_video, name='reg_stud'),
	path('<int:ID>', views.play, name='play'),
	path('history', views.history, name='history'),
	# path('allvideos', views.view_all, name='view_all'),
	path('rem/<int:ID>', views.remove_vid, name='remove'),
]
