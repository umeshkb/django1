from django.db import models
class Music(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=40)
    #published_date = models.DateTimeField(blank=True, null=True)

# Crea