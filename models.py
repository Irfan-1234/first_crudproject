from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        app_label = 'myapp'