from django.db import models

class Blog(models.Model):
    date = models.DateField(default = 'YYYY-MM-DD')
    student_name = models.CharField(max_length=100)
    uni_name = models.CharField(max_length=100)
    program_name = models.TextField(max_length=100)
    term = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    short_biography = models.TextField(max_length=400)
    interests_and_hobbies = models.TextField(max_length=250)
    image = models.ImageField(upload_to='blog/images', blank = True)
