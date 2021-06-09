from django.shortcuts import render

# Create your views here.
def student(request, branch):
	return render(request, 'dashboard/dashboard.html', {'student':True, 'teacher':False})
def teacher(request, branch):
	return render(request, 'dashboard/dashboard.html', {'student':False, 'teacher':True})