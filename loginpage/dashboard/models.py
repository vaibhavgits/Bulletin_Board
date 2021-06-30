from django.db import models

# Create your models here.
branch_choices = (
	('CSE', 'Computer science engineering'),
	('IT', 'Information technology'),
	('EE', 'Electrical and Electronics engineering'),
	('EC', 'Electronics and communication engineering'),
	('TandC', 'Training and placement'),
	('CE','Civil engineering'),
	('ME','Mechanical engineering'),
)
class FilesAdmin(models.Model):
	adminupload = models.FileField(upload_to = 'media')
	title = models.CharField(max_length = 50)
	branch = models.CharField(max_length = 50, choices = branch_choices)

	def __str__(self):
		return self.title + " " + self.branch