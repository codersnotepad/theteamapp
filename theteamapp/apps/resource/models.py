from django.db import models

# Create your models here.
ROLE_CHOICES = [
    ('AM', 'Assistant Manager'),
    ('M', 'Manager'),
    ('SM', 'Senior Manager'),
]

class Fact(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)
    employee_id = models.IntegerField(null=False,default=9999)
    role = models.CharField(max_length=20, unique=False, null=False, choices=ROLE_CHOICES)
    python = models.IntegerField(null=False,default=0)
    r = models.IntegerField(null=False,default=0)
    java = models.IntegerField(null=False,default=0)
    powerbi = models.IntegerField(null=False,default=0)
    datetime_added = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.name