from django.urls import path, include
from . import views

app_name = 'branchboard'
urlpatterns = [
	path('student', views.student),
	path('teacher', views.teacher),
	path('dashboard/', include('dashboard.urls')),
]