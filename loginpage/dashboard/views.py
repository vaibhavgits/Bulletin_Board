from django.shortcuts import render
from .models import FilesAdmin
# Create your views here.
def student(request, branch):
	return render(request, 'dashboard/dashboard.html', {'student':True, 'teacher':False, 'branch': request.path[21:24],'file':FilesAdmin.objects.all()[::-1]})
def teacher(request, branch):
	return render(request, 'dashboard/dashboard.html', {'student':False, 'teacher':True, 'branch': request.path[21:24],'file':FilesAdmin.objects.all()[::-1]})