from django.shortcuts import render

# Create your views here.
def student(request):
	return render(request, 'branchboard/board.html', {'student':True, 'teacher':False})
def teacher(request):
	return render(request, 'branchboard/board.html', {'student':False, 'teacher':True})