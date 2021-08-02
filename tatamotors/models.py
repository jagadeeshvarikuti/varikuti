from django.db import models

# Create your models here.
class studentaddress1(models.Model):
	ROLLNO = models.CharField(max_length = 200,null = True)
	NAME = models.CharField(max_length = 200,null = True)
	FATHERNAME = models.CharField(max_length = 200, null = True)
	STUDYING = models.CharField(max_length = 200, null = True)
	ADDRESS= models.CharField(max_length = 200, null = True)
	PHONENO= models.CharField(max_length = 200, null = True)
	img= models.ImageField(upload_to='tatamotors/')
	Create_at = models.DateTimeField(auto_now_add=True)
	
	
	
	def __str__(self):
		return self.NAME
class Meta:
 	#db_table = ''
 	#managed = 'True'
 	verbose_name = 'studentaddress1'
 	verbose_name_pural = 'studentaddress1s'		
		

