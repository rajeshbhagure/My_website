from django.db import models

# Create your models here.


class PersonalModel(models.Model):
    name=models.CharField(max_length=30)
    profile=models.CharField(max_length=30)
    email=models.EmailField()
    contact_number=models.IntegerField()
    Education=models.CharField(max_length=50)




class SkillModel(models.Model):
    skill_name=models.CharField(max_length=30)
    percentage=models.IntegerField()



class PortfolioModel(models.Model):
    image=models.ImageField(upload_to='portfolio')
    name=models.CharField(max_length=30)
    technology=models.CharField(max_length=30)
    date=models.DateField()


class BlogModel(models.Model):
    image=models.ImageField(upload_to='blog/')
    name=models.CharField(max_length=15)
    short_title=models.CharField(max_length=50)
    description=models.CharField(max_length=300)

