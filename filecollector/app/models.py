from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)



    class Meta:
        db_table = "users"
class files(models.Model):
    id=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    file=models.FileField(upload_to="files")



    class Meta:
        db_table = "files"