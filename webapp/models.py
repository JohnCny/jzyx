from django.db import models
from django.contrib import admin

# Create your models here.

class cardtype(models.Model):
    type=models.CharField(max_length=16)
   	 
    def __unicode__(self):
        return self.id
        
       
class customer(models.Model):

	LEVEL_CHOICES=(
		(0,"First"),
		(1,"Second")
	)

	customerno=models.CharField(max_length=20)
	cardtype=models.CharField(max_length=1)
	cardnumber=models.CharField(max_length=32)
	name=models.CharField(max_length=16)
	mobilephone=models.CharField(max_length=16)
	level=models.IntegerField(choices=LEVEL_CHOICES,default=1)
	deposit=models.DecimalField(max_digits=12,decimal_places=2)
	credit=models.DecimalField(max_digits=12,decimal_places=2)
	dintegration=models.DecimalField(max_digits=12,decimal_places=2)
	cintegration=models.DecimalField(max_digits=12,decimal_places=2)
	amountoffp=models.DecimalField(max_digits=12,decimal_places=2)
    
	def __unicode__(self):
		return self.customerno
    
class myfilter(models.Model):
    levelno=models.CharField(max_length=2)
    deposit=models.IntegerField()
    credit=models.IntegerField()
    dintegration=models.IntegerField()
    cintegration=models.IntegerField()
    amountoffp=models.IntegerField()
    industry=models.CharField(max_length=10)
    other=models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.levelno
    
class marketing(models.Model):
    levelno=models.CharField(max_length=2)
    type=models.CharField(max_length=2)
    path=models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.levelno

admin.site.register(myfilter)
