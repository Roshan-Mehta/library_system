from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,
        primary_key=True,)
	description=models.CharField(max_length=100,default='')
	city=models.CharField(max_length=100,default='')
	website=models.URLField(default='')
	phone=models.IntegerField(default=0)

class books(models.Model):
	bookID=models.IntegerField(default =0)
	title=models.CharField(max_length=1500,default='')
	authors=models.CharField(max_length=100,default='')
	average_rating=models.DecimalField(max_digits =5,decimal_places =4,default=0.0)
	isbn=models.CharField(max_length=100,default='')
	isbn13=models.CharField(max_length=100,default='')
	language_code=models.CharField(max_length=100,default='')
	num_pages=models.IntegerField(default =0)
	ratings_count=models.IntegerField(default =0)
	text_reviews_count=models.IntegerField(default = 0)
	publication_date=models.CharField(max_length=100,default='')
	publisher=models.CharField(max_length=100,default='')
