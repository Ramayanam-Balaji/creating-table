from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField()
    dname=models.CharField(max_length=100,primary_key=True)
    loc=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.dname
class Emp(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.ename

