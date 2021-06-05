from django.shortcuts import render

# Create your views here.
def student(request):
	return render(request, 'dashboard/dashboard.html', {'student':True, 'teacher':False})
def teacher(request):
	return render(request, 'dashboard/dashboard.html', {'student':False, 'teacher':True})