# from django.db import models

# # Create your models here.
# class category(models.Model):
#     category_name=models.CharField(max_length=100)

# # class book(models.Model):
# #     category=models.ForeignKey(category,on_delete=models.CASCADE)
# #     book_title=models.TextField(max_length=100)

# class book(models.Model):
#     category = models.ForeignKey(category, on_delete=models.CASCADE)
#     book_title = models.TextField(max_length=100)



# class student(models.Model):
#     name=models.CharField(max_length=100)
#     age=models.IntegerField()
#     father=models.CharField(max_length=100)

# models.py
from django.db import models

class category(models.Model):
    category_name = models.CharField(max_length=100)

class book(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    book_title = models.TextField(max_length=100)

class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    father = models.CharField(max_length=100)
