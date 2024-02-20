from django.db import models

# Create your models here.

class staffmembers(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    staff_title = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name
    
class bireports(models.Model):
    report_name = models.CharField(max_length=255, null=True)
    report_description = models.CharField(max_length=1000, null=True)
    report_link = models.CharField(max_length=1000, null=True)
    report_department = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self) -> str:
        return self.report_name